from typing import List, Tuple
from random import randint

"""
Author: William Noonan
        
        CSCI 5343 - Algorithms
        Assignment 3 - Priority Queue
        20 Feb 2022
        
        This file contains the implementations of the pseudocode for Max-Heap-Insert, Heap-Increase-Key, Heap-Extract-Max,
        Max-Heapify algorithms.
        Run the function 'main' or 'displayPriorityQueue' to see a max-heap for the priority queue of 100 randomly 
        generated numbers before and after ExtractMax operation.
"""


def getParent(i: int) -> int:
    """Returns the index of the parent of node index i"""
    return (i - 1) // 2  # corrected for zero-based indexing


def getLeft(i: int) -> int:
    """Returns the index of the node to the left of node index i"""
    return 2 * i + 1  # corrected for zero-based indexing


def getRight(i: int) -> int:
    """Returns the index of the node to the right of node index i"""
    return 2 * i + 2  # corrected for zero-based indexing


def heapIncreaseKey(A: List[int], i: int, key: int) -> None:
    """
    Given a key value key, max heap A, and node index i, ensure key is greater than current key at i, update current key at i with
    key, traverse the tree upward comparing each node key to that of its parent, swapping keys if necessary until child's
    key is less than parent's key.
    :param A: list of integers representing a max heap
    :param i: index in which to insert key
    :param key: integer
    :return: None (modifies A)
    """
    if key < A[i]:
        raise ValueError("new key is smaller than current key")
    A[i] = key
    while i > 0 and A[getParent(i)] < A[i]:
        A[i], A[getParent(i)] = A[getParent(i)], A[i]
        i = getParent(i)


def maxHeapInsert(A: List[int], key: int) -> None:
    """
    Inserts a key into a max heap.
    :param A: list of integers representing a max heap
    :param key: integer to insert into A
    :return: None (modifies A)
    """
    A.append(-999)
    heapIncreaseKey(A, len(A) - 1, key)


def heapExtractMax(A: List[int]) -> int:
    """
    Removes and returns the element of A with the largest key.
    :param A:
    :return:
    """
    if len(A) < 2:
        raise Exception("heap underflow")
    max_val = A[0]
    A[0] = A.pop()  # pop last element in A, put in first index
    maxHeapify(A, 0)
    return max_val


def maxHeapify(A: List[int], i: int) -> None:
    """
    Maintains max-heap property.
    :param A: list of integers representing a max heap
    :param i: index of subtree rooted at i
    :return: None (modifies A)
    """
    l: int = getLeft(i)
    r: int = getRight(i)
    largest: int = i
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # pythonic swap operation
        maxHeapify(A, largest)


def buildMaxHeapFromNRandInts(n=100) -> Tuple[List[int], List[int]]:
    """
    Creates a max heap from n random integers between 0 and 500 (inclusive).
    :param n: number of random integers to generate
    :return: max heap (list of integers)
    """
    raw = []
    A = []
    for i in range(n):
        key = randint(0, 500)
        raw.append(key)
        maxHeapInsert(A, key)
    return A, raw


def displayPriorityQueue() -> None:
    """
    This displays the max-heap for the priority queue before and after the max key extraction as described in the assignment.
    It prints the following:
        1) A list of 100 randomly generated numbers between 0 and 500 inclusive
        2) A maximum heap priority queue created from the list of 100 randomly generated numbers
        3) The extracted maximum value from the max heap
        4) The max heap after the max heap value has been extracted

    """
    A, raw = buildMaxHeapFromNRandInts(100)
    template = f"""Raw Data\n{raw}\n\nHeapified\n{A}\n\nDemonstrate ExtractMax\nExtracted max is {heapExtractMax(A)}\n\nHeap after ExtractMax\n{A}"""
    print(template)


def main():
    """
    This function handles command-line arguments. If no positional or optional arguments given, displayPriorityQueue is called.

    If optional argument -n followed by an integer is given, buildMaxHeapFromNRandInts is called and the heap is displayed.
        python heapify.py [-n 10]

    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int)
    args = parser.parse_args()
    if args.n:
        max_heap, _ = buildMaxHeapFromNRandInts(n=args.n)
        print(max_heap)
    else:
        displayPriorityQueue()


if __name__ == "__main__":
    main()
