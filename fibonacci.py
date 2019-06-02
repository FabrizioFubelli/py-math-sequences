#!/usr/bin/env python2

"""
Calculates the nth number of Fibonacci sequence
Reference: https://github.com/Dvd848/CTFs/blob/master/2018_picoCTF/be-quick-or-be-dead-2.md
"""

from ctypes import *
import numpy as np, sys

np.seterr(all="ignore")

class Memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret

@Memoize
def fib(n):
    if n == 0:
        return np.uint32(0)
    elif n == 1:
        return np.uint32(1)
    return fib(n-2) + fib(n-1)

def usage():
    print("Usage: ./fibonacci.py <int>        # Calculates the nth number of Fibonacci sequence")

def main():
    if len(sys.argv) != 2:
        usage()
        exit(1)
    try:
        requested_number = int(sys.argv[1])  # Es. 1067 => 781077913
    except:
        usage()
        exit(2)
    for i in range(requested_number): fib(i)
    print(fib(requested_number))
    exit(0)

if __name__ == "__main__":
    main()
