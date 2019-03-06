# Gridworld parameters
NUM_STATES = 54
NUM_ACTIONS = 4

START_STATE = 48
GOAL_STATE = 8
MIN_STEPS_TO_GOAL = 16
OBSTACLE_SHIFT_STEP = 1000   # Step number to shift the obstacle

# Plot parameters
PLOT_X_LIMIT = 100
PLOT_Y_LIMIT = 50

# Q-Learning
DISCOUNT = 0.95

# Single agent Q-Learning parameters
NUM_EPISODES = 100
EPSILON = 20     # Percent chance of choosing a random action
STEP_SIZE = 0.7

# Asynchronous Q-Learning parameters
BASE_MAX_STEPS = 5000   # Multiplied by the number of processes
ASYNC_EPSILON = 15
ASYNC_STEP_SIZE = 0.15
EPISODE_LENGTH = 100
ASYNC_UPDATE = 5

# NUM_PROCESS
FIRST_ASYNC_NUM_PROCESSES = 5
SECOND_ASYNC_NUM_PROCESSES = 55
THIRD_ASYNC_NUM_PROCESSES = 100
