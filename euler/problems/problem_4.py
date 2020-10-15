# https://projecteuler.net/problem=4
#
# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.


def solve(digit):
    for i in range(max_number_of_n_digits(digit) ** 2, min_number_with_n_digits(digit) ** 2, -1):
        if is_palindromic(i) and is_number_has_n_digits_factors(i, digit):
            return i


def min_number_with_n_digits(digit):
    return int('1' + '0' * (digit - 1))


def max_number_of_n_digits(digit):
    return int('9' * digit)


def is_palindromic(x: int) -> bool:
    x = str(x)
    y = len(x) // 2
    return x[0:y] == x[-1:-y - 1:-1]


def is_number_has_n_digits_factors(x: int, digits: int):
    return bool(set(i for i in range(min_number_with_n_digits(digits), max_number_of_n_digits(digits) + 1) if
                    x % i == 0 and len(str(x // i)) == digits))
