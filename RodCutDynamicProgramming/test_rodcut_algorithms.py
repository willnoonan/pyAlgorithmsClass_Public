import unittest
from rodcut_algorithms import memoizedCutRod, extendedBottomUpCutRod

class MyTestCase(unittest.TestCase):
    """
    Unit tests for the algorithms in rodcut_algorithms.py.
    """

    def setUp(self) -> None:
        self.p1 = [3, 5, 7, 8, 9]


    def test_memoizedCutRod(self):
        p = self.p1
        self.assertEqual(memoizedCutRod(p, 1)[0], 3)  # add assertion here
        self.assertEqual(memoizedCutRod(p, 2)[0], 6)  # add assertion here
        self.assertEqual(memoizedCutRod(p, 3)[0], 9)  # add assertion here
        self.assertEqual(memoizedCutRod(p, 4)[0], 12)  # add assertion here
        self.assertEqual(memoizedCutRod(p, 5)[0], 15)  # add assertion here

    def test_extendedBottomUpCutRod(self):
        p = self.p1
        # extendedBottomUpCutRod -> Tuple[List[int], List[int], int]
        self.assertEqual(extendedBottomUpCutRod(p, 1)[0][-1], 3)  # add assertion here
        self.assertEqual(extendedBottomUpCutRod(p, 2)[0][-1], 6)  # add assertion here
        self.assertEqual(extendedBottomUpCutRod(p, 3)[0][-1], 9)  # add assertion here
        self.assertEqual(extendedBottomUpCutRod(p, 4)[0][-1], 12)  # add assertion here
        self.assertEqual(extendedBottomUpCutRod(p, 5)[0][-1], 15)  # add assertion here



if __name__ == '__main__':
    unittest.main()
