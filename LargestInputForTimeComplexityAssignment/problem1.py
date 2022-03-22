from typing import List
from problem2 import findRoot
import math
import matplotlib.pyplot as plt
import numpy as np  # you may need to install this

"""
Author: William Noonan
This file contains the code I used for problem 1 of homework assignment 1.
I imported the root-finding function from problem2.py.
"""

def plotSortingAlgs():
    """
    This function plots the number of steps taken as a function of input size and sorting algorithm,
    insertion sort and merge sort.

    :return:
    """
    n = np.arange(1, 51)  # input size
    y1 = np.array([8 * x**2 for x in n])  # insertion sort steps
    y2 = np.array([64 * x * math.log(x, 2) for x in n])  # merge sort steps
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(n, y1, label="insertion sort")  # Plot some data on the axes.
    ax.plot(n, y2, label="merge sort")
    ax.set_xlabel("input size")
    ax.set_ylabel("steps")
    ax.legend()
    plt.show()


def findPointOfIntersection():
    """
    Here I use Newton's method (findRoot) to find where insertion sort and merge sort intersect.

    8n^2 == 64nlogn --> n^2 == 8nlogn --> n == 8logn
    For Newton's method, f(n) = 8logn - n, df(n) = 8/n - 1

    :return:
    """
    res = findRoot(lambda n: 8 * math.log(n, 2) - n, lambda n: 8/n - 1, floor=False)
    print(f"Insertion sort and merge sort intersect at n == {round(res, 3)}")


def main():
    """
    Problem statement:
        Suppose we are comparing implementations of insertion and merge sort on the same machine. For inputs size of n,
        insertion sort runs in 8n^2 steps, while merge sort runs in 64nlogn steps. For which values of n does insertion
        sort beat merge sort?

    My approach:
        I plot the steps taken by insertion sort and merge sort for various input sizes n, and I use Newton's method to
        approximate the value of n where they intersect.

    :return:
    """
    findPointOfIntersection()
    plotSortingAlgs()


if __name__ == "__main__":
    main()
