import unittest

from euler.problems.problem_1 import solve
from .helpers import solution_time


class SolutionTestCase(unittest.TestCase):
    condition = 1000
    answer = 233168

    def test_solution_with_default_condition(self):
        self.assertEqual(solve(10), 23)

    def test_solution(self):
        self.assertEqual(self.answer, solve(self.condition))

    def test_solution_time(self):
        solution_time(self, solve, self.condition)


if __name__ == '__main__':
    unittest.main()
