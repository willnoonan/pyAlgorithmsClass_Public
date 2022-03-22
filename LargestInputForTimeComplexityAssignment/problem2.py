from typing import List
import math
from collections import OrderedDict
import numpy as np
import pandas

"""
Author: William Noonan
This file contains the code I used for problem 2 of homework assignment 1.

Problem statement:
    For each function f(n) and time t in the following lists, determine the largest size n of a problem that can be
    solved in time t, assuming that the algorithm to solve the problem takes f(n) milliseconds.

    f(n) = [ log(n), sqrt(n), n, n*log(n), n^2, n^3, 2^n, n! ]
    t = [ 1 sec, 1 minute, 1 hour, 1 day, 1 month ]

My approach:
    For many of the functions, their inverse is easily found. But for a few, an approximation is needed.
    I learned about Newton's method in a numerical analysis class during my aerospace engineering undergrad.
    It is a root-finding algorithm that produces successively better approximations to the roots of a real-valued
    function. The algorithm terminates when f(xn) -- where f is the function and xn is the next approximation of the
    root -- yields a value within a margin of error, epsilon, typically 0.0001.

"""


def find_root_factorial(t):
    """
    Finds the root of n! using Newton's method on Stirling's approximation of n!.
    :param t: Time
    :return: The root of n*log(n) - t
    """
    func = lambda x: (x + 1/2) * math.log(x, 2) - x + 1/2 * math.log(2 * math.pi, 2) - math.log(t, 2)
    derivFunc = lambda x: math.log(x, 2) + 1/2 * 1/x
    res = findRoot(func, derivFunc)
    return res

def find_root_nlogn(t):
    """
    Finds the root of n*log(n) using Newton's method.
    :param t: Time
    :return: The root of n*log(n) - t
    """
    func = lambda x: x * math.log(x, 2) - t
    derivFunc = lambda x: 1 + math.log(x, 2)
    res = findRoot(func, derivFunc)
    return res

def findRoot(func, derivFunc, x0=10, epsilon=0.0001, max_iter=1000, floor=True, verbose=False):
    """
    Newton's method to find the root (zero) of a function.
    :param func: Function to find root of
    :param derivFunc: Derivative of func
    :param x0: Initial guess
    :param epsilon: Margin of error
    :param max_iter: Max iterations allowed
    :param floor: If True, findRoot returns the floor of the calculation
    :param verbose: Prints number of iterations used
    :return: Root of func
    """
    xn = x0
    for n in range(max_iter):
        fxn = func(xn)
        if abs(fxn) < epsilon:
            if verbose:
                print(f"Found solution after {n} iterations.")
            return math.floor(xn) if floor else xn
        dfxn = derivFunc(xn)
        if dfxn == 0:
            print("Zero derivative. No solution found.")
            return None
        xn = xn - fxn / dfxn
    print("Exceeded maximum iterations. No solution found.")
    return None


def main():
    """
    Problem statement:
        For each function f(n) and time t in the following lists, determine the largest size n of a problem that can be
        solved in time t, assuming that the algorithm to solve the problem takes f(n) milliseconds.

        f(n) = [ log(n), sqrt(n), n, n*log(n), n^2, n^3, 2^n, n! ]
        t = [ 1 sec, 1 minute, 1 hour, 1 day, 1 month ]

    My approach:
        For many of the functions, their inverse is easily found. But for a few, an approximation is needed.
        I learned about Newton's method in a numerical analysis class during my aerospace engineering undergrad.
        It is a root-finding algorithm that produces successively better approximations to the roots of a real-valued
        function. The algorithm terminates when f(xn) -- where f is the function and xn is the next approximation of the
        root -- yields a value within a margin of error, epsilon, typically 0.0001.

    """

    # Array of input run times converted to milliseconds (1 s == 1000 ms):
    time_ms = 1000 * np.array([1, 60, 60*60, 24*60*60, 30*24*60*60], dtype=float)

    # Ordered dictionary of f(n) and associated inverse or Newton's-method function:
    funcmap = OrderedDict()
    funcmap["log(n)"] = lambda t: 2**t
    funcmap["sqrt(n)"] = lambda t: math.floor(t**2)
    funcmap["n"] = lambda t: math.floor(t)
    funcmap["n*log(n)"] = find_root_nlogn
    funcmap["n^2"] = lambda t: math.floor(math.sqrt(t))
    # funcmap["n^3"] = lambda t: round(math.pow(t, 1/3))  # n^3 -> [10, 39, 153, 442, 1374]  last value is wrong, should be 1373
    funcmap["n^3"] = lambda t: findRoot(lambda n: n**3 - t, lambda n: 3*n**2)  # Newton's method gives correct roots for n^3
    funcmap["2^n"] = lambda t: math.floor(math.log(t, 2))
    funcmap["n!"] = find_root_factorial

    # Results:
    res = {key: [f(t) for t in time_ms] for key, f in funcmap.items()}

    # Conversion to string for printing:
    str_res = {key: [str(n) for n in val] for key, val in res.items()}

    # Conversion of dictionaries to a pandas Data Frame:
    columns = ["1 second", "1 minute", "1 hour", "1 day", "1 month"]
    df = pandas.DataFrame.from_dict(str_res, orient="index", columns=columns)

    # Print the Data Frame:
    print(df.to_string())

if __name__ == "__main__":
    main()
