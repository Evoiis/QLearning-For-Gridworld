import numpy
from scripts import constants


def q_learning(gridworld, plot):
    # Initialize q_table
    q_table = numpy.zeros(shape=(constants.NUM_STATES, constants.NUM_ACTIONS), dtype=float)
    total_reward = 0
    total_steps = 0
    epsilon = 100

    for episode in range(constants.NUM_EPISODES):
        state = constants.START_STATE
        terminal = False
        while not terminal:
            plot.insert_data(total_reward)

            action = choose_action(q_table, epsilon, state)

            reward, new_state = gridworld.move_player(action, state)
            total_steps += 1

            # Decrease epsilon at each step
            if epsilon >= 10.2:
                epsilon -= 0.2

            # Shift obstacle and reset epsilon to 100 after 1000 steps have been taken
            if total_steps == 1000:
                epsilon = 100
                total_reward = 0
                gridworld.move_obstacle()

            if reward != -1:
                q_table[state][action] += constants.STEP_SIZE * \
                                          (reward + constants.DISCOUNT * q_table[new_state].max() - q_table[state][action])

                if reward == 1:
                    total_reward += 1
                    terminal = True

                state = new_state

    plot.generate_plot()


# Choose action using epsilon greedy policy
def choose_action(q_table, epsilon, state):
    random = numpy.random.randint(0, 101)
    if random < epsilon:
        action = numpy.random.randint(constants.NUM_ACTIONS)
    else:
        action = q_table[state].argmax()
    return action
