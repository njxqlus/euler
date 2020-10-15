import unittest

from euler.problems.problem_4 import solve, is_palindromic
from .helpers import solution_time


class SolutionTestCase(unittest.TestCase):
    condition = 3
    answer = 906609

    def test_is_palindromic(self):
        self.assertTrue(is_palindromic(9009))
        self.assertTrue(is_palindromic(90109))
        self.assertTrue(is_palindromic(101))
        self.assertTrue(is_palindromic(11))

    def test_default_condition(self):
        self.assertEqual(9009, solve(2))

    def test_solution(self):
        self.assertEqual(self.answer, solve(self.condition))

    def test_solution_time(self):
        solution_time(self, solve, self.condition)


if __name__ == '__main__':
    unittest.main()
