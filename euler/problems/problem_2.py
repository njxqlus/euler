# https://projecteuler.net/problem=2
#
# Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
#
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.


def solve(x: int) -> int:
    a = 1
    b = 2
    r = 0
    while r <= x:
        if not a & 1:
            r += a
        a, b = b, a + b
    return r


def solve_2(x: int) -> int:
    """
    We know that every third fibonacci number is even
    This solution is more faster
    """
    a = 1
    b = 2
    r = 0
    i = 2
    while r <= x:
        a, b, i = b, a + b, i + 1
        if i == 3:
            r, i = r + a, 0
    return r
