# https://projecteuler.net/problem=3
#
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# Простые делители числа c - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

from math import sqrt


def solve(x: int) -> int:
    for i in range(int(sqrt(x) + 1), 2, -1):
        if x % i == 0 and is_prime(i):
            return i


def is_prime(x: int) -> bool:
    return all(x % i != 0 for i in range(2, int(sqrt(x) + 1)))


def solve_2(x: int) -> int:
    """
    Dramatically faster solution using fundamental theorem of arithmetic
    Source: https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p003.py
    """
    while True:
        # Find smallest prime factor
        p = smallest_prime_factor(x)
        if p < x:
            # by the fundamental theorem of arithmetic (https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)
            # every integer n > 1 has a unique factorization as a product of prime numbers
            # Because of that we can divide x by smallest prime number to decrease search range
            x //= p
        else:
            return x


def smallest_prime_factor(x):
    # 2 is the smallest prime for this task.
    # Using sqrt(x) instead of x described here: https://stackoverflow.com/a/27946768
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return i
    # returning x mean that not any prime factor found
    return x
