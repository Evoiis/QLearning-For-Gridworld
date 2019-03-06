#!/usr/bin/env python
import unittest

from scripts import constants, gridworld


class QLearnTest(unittest.TestCase):

    def setUp(self):
        self.test_gw = gridworld.GridWorld()

    def tearDown(self):
        pass

    def test_action_set(self):
        self.assertEqual(self.test_gw.action_set, [-9, 9, -1, 1])

    def test_obstacle(self):
        self.assertEqual(self.test_gw.obstacle, [26, 35])

    def test_check_next_state(self):

        # Goal state
        self.assertEqual(self.test_gw.check_next_state(constants.GOAL_STATE), 1)

        # Out of bound
        self.assertEqual(self.test_gw.check_next_state(-1), -1)
        self.assertEqual(self.test_gw.check_next_state(54), -1)

        # Moving into obstacle
        for i in range(self.test_gw.obstacle[0] + 1, self.test_gw.obstacle[1]):
            self.assertEqual(self.test_gw.check_next_state(i), -1)

        # All states excluding the obstacle states or goal state
        for j in range(0, self.test_gw.obstacle[0]):
            if j != constants.GOAL_STATE:
                self.assertEqual(self.test_gw.check_next_state(j), 0)
        for k in range(self.test_gw.obstacle[1], 54):
            if k != constants.GOAL_STATE:
                self.assertEqual(self.test_gw.check_next_state(k), 0)

    def test_check_current_state(self):
        self.assertEqual(self.test_gw.check_current_state(2, 9), -1)
        self.assertEqual(self.test_gw.check_current_state(3, 8), -1)

        self.assertEqual(self.test_gw.check_current_state(3, 1), 0)

    def test_move_player(self):
        # Move off left side of map
        self.assertEqual(self.test_gw.move_player(2, 9), (-1, 9))

        # Move off left side of map
        self.assertEqual(self.test_gw.move_player(3, 8), (-1, 8))

        # Move into goal state
        self.assertEqual(self.test_gw.move_player(3, 7), (1, 8))

        self.assertEqual(self.test_gw.move_player(3, 1), (0, 2))

        self.assertEqual(self.test_gw.move_player(0, 1), (-1, -8))

    def test_move_obstacle(self):
        self.test_gw.move_obstacle()

        self.assertEqual(self.test_gw.obstacle, [27, 36])


if __name__ == '__main__':
    unittest.main()
