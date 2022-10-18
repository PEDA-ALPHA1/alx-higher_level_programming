#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_neg_int(self):
        self.assertEqual(max_integer([-8, -9, -1]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([9, 7, 0, 3, 1]), 9)
        self.assertEqual(max_integer([1, 2, 8, 5, 4]) ,8)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)


'''must always include "test" pamamethod names otherwise the tests wont run
'''
if __name__ == '__main__':
    unittest.main()
