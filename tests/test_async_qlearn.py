#!/usr/bin/env python
import unittest
import numpy

from multiprocessing import Array
from scripts.async_qlearning import async_qlearn


class QLearnTest(unittest.TestCase):

    def setUp(self):
        print "Start async_qlearn test"
        self.test_array = Array('f', numpy.zeros(shape=16, dtype=float))
        self.filter_test_array = Array('f', numpy.zeros(shape=16, dtype=int))

    def tearDown(self):
        pass

    def test_get_max_q(self):
        self.test_array[2] = 2
        self.assertEqual(async_qlearn.get_max_q(self.test_array, 0), 2)

        self.test_array[15] = 15
        self.assertEqual(async_qlearn.get_max_q(self.test_array, 3), 15)

    def test_filter_array(self):
        number = 2
        result_list = []
        expected_list = range(0, 14, 2)

        for j in range(7):
            expected_list[j] /= number

        for i in range(0, 14, 2):
            self.filter_test_array[i] = i
            self.filter_test_array[i + 1] = number

        async_qlearn.filter_array(number, 16, self.filter_test_array, result_list)

        self.assertEqual(expected_list, result_list)


if __name__ == '__main__':
    unittest.main()
