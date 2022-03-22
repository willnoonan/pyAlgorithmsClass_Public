from typing import List
from random import randint

"""
Author: William Noonan

        CSCI 5343 - Algorithms
        Assignment 2
        9 Feb 2022
        
        This file contains an implementation of the Find Maximum Subarray algorithm and associated functions. 
        Run function 'main' (which runs by default if this script is run) to see the results for 100 days of random daily prices. 
        
        The algorithm in recurseFindMaxSubarray (wrapped by findMaxSubarray) solves the maximum-subarray problem using 
        the divide-and-conquer technique to find a contiguous subarray whose values have the largest sum.
        It looks for the maximum subarray in three places: 1) entirely in the subarray A[lo..mid], 2) entirely in the 
        subarray A[mid+1..hi], 3) crossing the midpoint. It recursively finds max subarrays in the first two cases,
        but in time linear in the third case.
         
"""

def getPriceChanges(A: List[int]) -> List[int]:
    """
    Calculates a list of price changes for daily prices list A.

    :param A: list of integers
    :return: list of integers that are the price changes
    """
    return [A[i] - A[i - 1] for i in range(1, len(A))]


def findMaxCrossingSubarray(A, lo, mid, hi):
    """
    This function finds the maximum subarray that crosses the midpoint of A. This can be done in linear time.

    :param A: list of price changes
    :param lo: low index
    :param mid: mid index
    :param hi: high index
    :return: (max_left, max_right, left_sum + right_sum)
    """
    left_sum = -999_999  # using a[mid] might work too
    cur_sum = 0
    max_left = mid
    # for i = mid downto lo
    for i in reversed(range(lo, mid+1)):
        cur_sum = cur_sum + A[i]
        if cur_sum > left_sum:
            left_sum = cur_sum
            max_left = i

    right_sum = -999_999  # using a[mid+1] might work too
    cur_sum = 0
    max_right = mid + 1
    for j in range(mid+1, hi+1):
        cur_sum = cur_sum + A[j]
        if cur_sum > right_sum:
            right_sum = cur_sum
            max_right = j

    return max_left, max_right, left_sum+right_sum


def recurseFindMaxSubarray(A, lo, hi):
    """
    This solves the maximum-subarray problem using the divide-and-conquer technique.
    It looks for the maximum subarray in three places: 1) entirely in the subarray A[lo..mid], 2) entirely in the
    subarray A[mid+1..hi], 3) crossing the midpoint.

    This funciton is wrapped by the findMaxSubarray function below.

    :param A: list of price changes
    :param lo: low index
    :param hi: high index
    :return: tuple of low index, high index, and maximum subarray sum (profit)
    """
    if hi == lo:
        return lo, hi, A[lo]
    else:
        mid = (lo + hi) // 2
        left_lo, left_hi, left_sum = recurseFindMaxSubarray(A, lo, mid)
        right_lo, right_hi, right_sum = recurseFindMaxSubarray(A, mid + 1, hi)
        cross_lo, cross_hi, cross_sum = findMaxCrossingSubarray(A, lo, mid, hi)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_lo, left_hi, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_lo, right_hi, right_sum
        else:
            return cross_lo, cross_hi, cross_sum


def findMaxSubarray(A):
    """
    Wrapper for recurseFindMaxSubarray; increments the values of the indices returned by
    recurseFindMaxSubarray, because the list of price changes is one element shorter than the list of daily prices,
    and because recurseFindMaxSubarray assumes zero-based indexing for its input array.

    :param A: array of integers
    :return: (max_lo + 1, max_hi + 1, max_sum)  # where max_lo, max_hi, max_sum are the values returned by recurseFindMaxSubarray
    """
    max_lo, max_hi, max_sum = recurseFindMaxSubarray(A, 0, len(A) - 1)
    return max_lo + 1, max_hi + 1, max_sum


def formatStrIntList(intlist, size=3):
    """
    Generates a string of a list of integers where each element is left-padded according to arg size.

    :param intlist: list of integers
    :param size: size of empty string left-padding
    :return:
    """
    fmtstr = "{:" + f"{size}" + "}"
    strs = [fmtstr.format(n) for n in intlist]
    return "[" + ", ".join(strs) + "]"


def formatStrAsteriskIndexList(length, first, last, size=3):
    """
    Generates a string of a list of empty strings except for the indices between args first and last, which contain
    asterisks.

    :param length: length of list
    :param first: first index where an asterisk is to appear
    :param last: last index where an asterisk is to appear
    :param size: size of list element string padding (default is 3)
    :return: a string of a list of empty strings with asterisks between indices first and last
    """
    fmtstr = "{:>" + f"{size}" + "}"
    str_list = [" "*size for _ in range(length)]
    for i in range(first, last+1):
        str_list[i] = fmtstr.format("*")
    return "[" + ", ".join(str_list) + "]"


def printMaxSubarrayFromDailyPrices(daily_prices):
    """
    This function takes a list of daily prices as input and prints them, then the list of its price changes, then
    a list with asterisks marking the maximum subarray, and then the tuple of values returned by findMaxSubarray.

    :return: None (prints inputs and outputs)
    """
    price_changes = getPriceChanges(daily_prices)
    res = findMaxSubarray(price_changes)
    max_lo, max_hi, _ = res
    print("Daily prices:         ", formatStrIntList(daily_prices))  # print daily prices as first row
    print("Price changes:        ", formatStrIntList([0] + price_changes))  # print price changes as second row (must add a 0 to the left to align output with the daily prices)
    print("Max-subarray location:", formatStrAsteriskIndexList(len(daily_prices), max_lo, max_hi))  # print list with asterisks that mark the subarray
    print("Max-subarray low-index, high-index, profit ==", res)  # print tuple of low and high indices of subarray, and max profit


def main():
    """
    This runs findMaxSubarray for 100 days of random daily prices by calling printMaxSubarrayFromDailyPrices, which
    first calls getPriceChanges to convert the daily prices to price changes, then prints the inputs and outputs.

    """
    num_days = 100  # number of days
    low_price, high_price = 50, 120  # low and high prices specified in assignment
    # daily_prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]  # for testing
    daily_prices = [randint(low_price, high_price) for _ in range(num_days)]  # daily random prices
    printMaxSubarrayFromDailyPrices(daily_prices)  # print the inputs and outputs



if __name__ == "__main__":
    main()
