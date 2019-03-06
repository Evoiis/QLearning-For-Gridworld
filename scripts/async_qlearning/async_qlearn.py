import numpy
from multiprocessing import Process, Lock, Array, Value

from scripts import gridworld, constants


def init_async_q_learning(num_processes):
    processes = []
    avg_total_reward = []       # Result list of average total reward at each ith step
    max_steps = constants.BASE_MAX_STEPS * num_processes

    counter_lock = Lock()
    q_table_lock = Lock()
    plot_data_lock = Lock()

    # Initialize shared arrays
    q_table = numpy.zeros(shape=(constants.NUM_STATES * constants.NUM_ACTIONS), dtype=float)
    plot_data = numpy.zeros(shape=(2 * (max_steps + 1)), dtype=float)
    shared_q_table = Array('f', q_table)
    shared_plot_data = Array('f', plot_data)
    shared_counter = Value('i', 0)

    print "Number of processes = ", num_processes, \
        "Max steps = ", max_steps, "Epsilon = ", constants.ASYNC_EPSILON, "Step size = ", constants.ASYNC_EPSILON

    print "Starting processes"

    for process_id in range(num_processes):
        gw = gridworld.GridWorld()

        new_process = Process(target=async_q_learning, args=(shared_q_table, shared_plot_data, shared_counter, q_table_lock, plot_data_lock, counter_lock, max_steps, gw))
        new_process.start()
        assert new_process.is_alive(), "Process " + str(process_id) + " Failed to start"

        processes.append(new_process)

    print "Waiting for processes to finish"

    for process in processes:
        process.join()

    print "Processes finished"

    filter_array(num_processes, 2 * max_steps, shared_plot_data, avg_total_reward)

    return avg_total_reward


def async_q_learning(shared_q_table, shared_plot_data, shared_counter, q_table_lock, plot_data_lock, counter_lock, max_steps, gw):
    updates = {}    # ('Index in shared_q_table': 'Update value')

    state = constants.START_STATE
    terminal = False
    end_process = False

    episode = 0
    total_steps = 0
    total_reward = 0

    while not end_process:
        # Choose action using epsilon greedy policy
        random = numpy.random.randint(0, 101)
        if random < constants.ASYNC_EPSILON:
            action = numpy.random.randint(constants.NUM_ACTIONS)
        else:
            # Get action with max Q
            action = state*4
            for i in range(1, 4):
                other_action = state*4 + i
                q_table_lock.acquire()
                if shared_q_table[action] < shared_q_table[other_action]:
                    action = other_action
                q_table_lock.release()
            action -= state*4

        # Take action
        reward, new_state = gw.move_player(action, state)

        # If move is valid, accumulate update
        if reward != -1:
            index = state*4 + action

            q_table_lock.acquire()
            if index in updates:
                updates[index] += (reward + constants.DISCOUNT * get_max_q(shared_q_table, new_state) - shared_q_table[index])
            else:
                updates[index] = (reward + constants.DISCOUNT * get_max_q(shared_q_table, new_state) - shared_q_table[index])
            q_table_lock.release()
            state = new_state

        # If reward received from Gridworld
        if reward == 1:
            total_reward += 1
            state = constants.START_STATE
            terminal = True

        # Add total episodic reward to plot data
        if (total_steps % constants.EPISODE_LENGTH) == 0:
            plot_data_lock.acquire()
            shared_plot_data[episode] += total_reward
            shared_plot_data[episode + 1] += 1
            plot_data_lock.release()
            episode += 2
            total_reward = 0

        total_steps += 1

        if (total_steps % constants.ASYNC_UPDATE) == 0 or terminal:
            # Update shared_q_table with accumulated updates
            q_table_lock.acquire()
            for index in updates:
                shared_q_table[index] += constants.ASYNC_STEP_SIZE * updates[index]
            q_table_lock.release()

            updates = {}
            terminal = False

        # Increment shared_counter
        counter_lock.acquire()
        shared_counter.value += 1
        value = shared_counter.value
        counter_lock.release()

        # Check if shared counter has exceeded max_steps or 1000
        if value > max_steps:
            end_process = True
        elif value >= 1000:
            # Tell gridworld to move obstacle
            gw.move_obstacle()


def filter_array(num_processes, max_step, array, avg_list):
    # Inserts average total episodic reward into list
    # Stops when the max_step has been reached or a step not visited by all processes is reached
    step = 0
    num_processes_reached_step = array[step + 1]
    while num_processes_reached_step == num_processes and step < max_step:
        reward_at_step = array[step] / num_processes_reached_step
        avg_list.append(reward_at_step)

        step += 2
        num_processes_reached_step = array[step + 1]


def get_max_q(array, state):
    max_q = 0.
    for i in range(4):
        q = array[state*4 + i]
        if q > max_q:
            max_q = q

    return max_q


if __name__ == '__main__':
    init_async_q_learning(100)
