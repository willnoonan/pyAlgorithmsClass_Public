"""
Author: William Noonan

        CSCI 5343 - Algorithms
        Assignment 2
        9 Feb 2022

        This file contains some unit tests for functions in maximum_subarray.py.
"""

import unittest

from maximum_subarray import getPriceChanges
from maximum_subarray import findMaxSubarray


class MyTestCase(unittest.TestCase):
    """
    These are unit tests for the functions in maximum_subarray.py.

    """

    def test_pricechanges_conversion(self):
        """
        This tests the function that converts a list of daily prices to a list of price changes.
        """
        A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        answer = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        self.assertEqual(getPriceChanges(A), answer)

    def test_examplecase_pricechanges(self):
        """
        This tests findMaxSubarray using the list of price changes in the example from lecture.
        """
        A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        self.assertEqual(findMaxSubarray(A), (8, 11, 43))

    def test_examplecase_dailyprices(self):
        """
        This tests findMaxSubarray by first converting the list of daily prices from the example in lecture to a
        list of price changes.
        """
        A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
        price_changes = getPriceChanges(A)
        self.assertEqual(findMaxSubarray(price_changes), (8, 11, 43))


if __name__ == '__main__':
    unittest.main()
