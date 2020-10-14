import sys
import time
import unittest

from euler.problems.problem_2 import solve, solve_2
from .helpers import solution_time, is_faster_solution


class SolutionTestCase(unittest.TestCase):
    condition = 4000000
    answer = 4613732

    def test_solution(self):
        self.assertEqual(self.answer, solve(self.condition))

    def test_solution_time(self):
        start_time = time.time()
        solve(self.condition)
        self.assertLess(time.time() - start_time, 60)


class Solution2TestCase(unittest.TestCase):
    condition = 4000000
    answer = 4613732

    def test_solution(self):
        self.assertEqual(self.answer, solve_2(self.condition))

    def test_solution_time(self):
        solution_time(self, solve, self.condition)

    def test_is_faster_solution(self):
        is_faster_solution(self, solve, solve_2, sys.maxsize)


if __name__ == '__main__':
    unittest.main()
