import unittest

from heapify import buildMaxHeapFromNRandInts
from heapify import heapExtractMax

"""
Author: William Noonan

        CSCI 5343 - Algorithms
        Assignment 3 - Priority Queue
        20 Feb 2022

        This file contains unit tests to test functions in heapify.py.
"""


class MyTestCase(unittest.TestCase):
    def test_PriorityQueue(self):
        """
        This unit test tests properties of a max-heap priority queue of 100 randomly generated numbers before and after
        extracting the max key by calling heapExtractMax.
        """
        # Before ExtractMax
        A, raw = buildMaxHeapFromNRandInts(n=100)  # the max heap and the raw list of 100 randomly generated integers
        self.assertEqual(len(A), 100)  # assert that there are 100 keys in A
        self.assertTrue(min(A) >= 0)  # assert that no key in A is less than 0
        self.assertTrue(max(A) <= 500)  # assert that no key in A is greater than 500
        self.assertEqual(A[0], max(A))  # assert that the first element in A is also the maximum key in A

        # After ExtractMax
        max_key = heapExtractMax(A)  # extract the max key
        self.assertEqual(max_key, max(raw))  # assert that the extracted key is the maximum of the raw list of keys
        self.assertEqual(len(A), 99)  # assert that the length of A is now 99
        self.assertEqual(A[0], max(A))  # assert that the first element in A is still the maximum key in A



if __name__ == '__main__':
    unittest.main()
