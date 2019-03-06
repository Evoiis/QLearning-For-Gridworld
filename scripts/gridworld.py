import constants


class GridWorld:

    def __init__(self):
        self.action_set = [-9, 9, -1, 1]  # Up, down, left, right
        self.obstacle = [26, 35]

    def check_next_state(self, state):
        # Check if moving off the top or bottom of map
        if state < 0 or state > 53:
            return -1

        # Check if moving into obstacle
        if self.obstacle[0] < state < self.obstacle[1]:
            return -1

        # Check if reached goal
        if state == constants.GOAL_STATE:
            return 1

        return 0

    def check_current_state(self, action, state):
        # Check if moving off the left or right side of map
        if (state % 9) == 0:
            if action == 2:
                return -1
        elif ((state + 1) % 9) == 0:
            if action == 3:
                return -1

        return 0

    def move_player(self, action, state):

        if self.check_current_state(action, state) == -1:
            return -1, state

        next_state = state + self.action_set[action]
        reward = self.check_next_state(next_state)

        return reward, next_state

    def move_obstacle(self):
        self.obstacle[0] = 27
        self.obstacle[1] = 36
