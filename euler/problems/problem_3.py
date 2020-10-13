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
