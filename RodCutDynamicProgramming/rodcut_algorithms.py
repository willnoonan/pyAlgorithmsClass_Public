from typing import List, Tuple
import sys

"""
Author: William Noonan

        CSCI 5343 - Algorithms
        Assignment 4
        13 Mar 2022

        This file contains implementations of the MEMOIZED-CUT-ROD and EXTENDED-BOTTOM-UP-CUT-ROD algorithms.
        
        Both algorithms were run for values of n from 1 to 7. The output shows that for each value of n, the number of
        recursive calls in MEMOIZED-CUT-ROD matches the number of iterations in EXTENDED-BOTTOM-UP-CUT-ROD.
        This makes sense because they are both O(n^2).
"""

INDENT = " " * 4  # indenting for printing


def memoizedCutRod(p: List[int], n: int) -> Tuple[int, int]:
    """
    This function implements the MEMOIZED-CUT-ROD algorithm by wrapping a class that is used to count the recursive
    calls.

    :param p: list of prices
    :param n: length of rod
    :return: optimal revenue and count of recursive calls
    """

    class _MemoizedCutRod:
        """This class is used to count the recursive calls in _memoizedCutRodAux."""
        def __init__(self):
            # counter var:
            self.counter = -1  # initialized to -1 so first call to recursive func is the zeroth call

        def _memoizedCutRodAux(self, p: List[int], n: int, r: List[int]) -> int:
            self.counter += 1
            if r[n] >= 0:
                return r[n]
            if n == 0:
                q = 0
            else:
                q = -999
                for i in range(1, n + 1):
                    q = max(q, p[i - 1] + self._memoizedCutRodAux(p, n - i, r))  # p has zero-based indexing
            r[n] = q
            return q

        def __call__(self, p: List[int], n: int, r: List[int]) -> Tuple[int, int]:
            """Wraps the Aux function. Allows you to call directly on an instance."""
            return self._memoizedCutRodAux(p, n, r), self.counter

    if n > len(p):
        raise ValueError(f"value of n exceeds length of rod -> {len(p)}")
    r = [-999] * (n + 1)
    return _MemoizedCutRod()(p, n, r)


def printMemoizedCutRodSolution(p, n):
    """
    Displays a table of the lengths and prices up to n, as well as optimal revenue and the number of recursive calls
    used to get the optimal revenue.

    :param p: list of prices
    :param n: length of rod
    :return: None (prints)
    """
    r, count = memoizedCutRod(p, n)
    print("MEMOIZED-CUT-ROD")
    size = 3
    fmtstr = "{:" + f"{size}" + "}"
    str1 = "length    i  |" + " ".join(fmtstr.format(i) for i in range(n + 1))
    print(INDENT + str1)
    print(INDENT + "price   p[i] | " + (" " * size) + " ".join(fmtstr.format(x) for x in p[0:n]))
    print(INDENT + "-" * len(str1))
    print(INDENT + "revenue r[i] |" + " ".join([fmtstr.format(memoizedCutRod(p, x)[0]) for x in range(n)] + [fmtstr.format(r)]))

    print()
    print(INDENT + "Rod length (n):")
    print(INDENT + str(n))
    print(INDENT + "Optimal revenue:")
    print(INDENT + str(r))
    print(INDENT + "Recursive calls:")
    print(INDENT + str(count))
    print()


"""
***
"""


def extendedBottomUpCutRod(p: List[int], n: int) -> Tuple[List[int], List[int], int]:
    """
    This function implements the EXTENDED-BOTTOM-UP-CUT-ROD algorithm.

    :param p: list of prices
    :param n: length of rod
    :return: list of revenues up to n, list of cut locations, count of iterations used
    """
    if n > len(p):
        raise ValueError(f"value of n exceeds length of rod -> {len(p)}")
    r = [0] * (n + 1)
    s = [1] * n
    count = 0
    for j in range(1, n + 1):
        q = -999
        for i in range(1, j + 1):
            count += 1
            if q < (p[i - 1] + r[j - i]):
                q = p[i - 1] + r[j - i]
                s[j - 1] = i
        r[j] = q
    return r, s, count


def printExtendedBottomUpCutRodSolution(p, n):
    """
    Displays a table of the lengths and prices up to n, as well as optimal revenue, decomposition, and the number of
    iterations used to get the optimal revenue.

    :param p: list of prices
    :param n: length of rod
    :return: None (prints)
    """
    r, s, count = extendedBottomUpCutRod(p, n)
    print("EXTENDED-BOTTOM-UP-CUT-ROD")
    size = 3
    fmtstr = "{:" + f"{size}" + "}"
    str1 = "length    i  |" + " ".join(fmtstr.format(i) for i in range(n + 1))
    print(INDENT + str1)
    print(INDENT + "price   p[i] | " + (" " * size) + " ".join(fmtstr.format(x) for x in p[0:n]))
    print(INDENT + "-" * len(str1))
    print(INDENT + "revenue r[i] |" + " ".join(fmtstr.format(x) for x in r))
    print()
    print(INDENT + "Rod length (n):")
    print(INDENT + str(n))
    print(INDENT + "Optimal revenue:")
    print(INDENT + str(r[-1]))

    # compute decomposition, the lengths of the subcomponents
    decomp = []
    i = n
    while i > 0:
        decomp.append(str(s[i - 1]))
        i = i - s[i - 1]

    print(INDENT + "Decomposition:")
    print(INDENT + ", ".join(decomp))
    print(INDENT + "Iterations:")
    print(INDENT + str(count))
    print()


def main():
    """
    Main function. Calls printMemoizedCutRodSolution and printExtendedBottomUpCutRodSolution.
    User enters the size of the rod.
    The output shows that the number of iterations and recursive calls are equal for each value of n.
    :return:
    """

    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # list of sample prices for each value n

    while True:
        try:
            n = int(input("Enter size of rod: "))  # size of the rod
        except ValueError:
            sys.exit()

        # print the MEMOIZED-CUT-ROD solution
        printMemoizedCutRodSolution(p, n)
        # print the EXTENDED-BOTTOM-UP-CUT-ROD solution
        printExtendedBottomUpCutRodSolution(p, n)


if __name__ == "__main__":
    main()
