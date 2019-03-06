#!/usr/bin/env python
import unittest
import numpy

from scripts import constants
from scripts.qlearning import qlearn


class QLearnTest(unittest.TestCase):

    def setUp(self):
        self.test_table = numpy.zeros(shape=(constants.NUM_STATES, constants.NUM_ACTIONS), dtype=float)

    def tearDown(self):
        pass

    def test_choose_action(self):
        state = 0
        action = 1
        self.test_table[state][action] = 1
        self.assertEqual(qlearn.choose_action(self.test_table, 0, state), action)


if __name__ == '__main__':
    unittest.main()
