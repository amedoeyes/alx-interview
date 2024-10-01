#!/usr/bin/python3

"""Prime Game"""


def get_primes(n):
    """Return a list of primes up to n"""
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primes


def isWinner(x, nums):
    """Prime Game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    ben = 0
    maria = 0
    for round in range(x):
        primes = get_primes(nums[round])
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben < maria:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
