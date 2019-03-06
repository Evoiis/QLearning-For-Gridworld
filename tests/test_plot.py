#!/usr/bin/env python
import unittest

from scripts import constants, plot


class QLearnTest(unittest.TestCase):

    def setUp(self):
        self.test_plot = plot.Plot()

    def tearDown(self):
        pass

    def test_data(self):
        self.assertEqual(self.test_plot.data, [])

    def test_insert_data(self):
        self.test_plot.insert_data(1)
        self.assertEqual(self.test_plot.data, [1])


if __name__ == '__main__':
    unittest.main()
