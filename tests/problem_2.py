import unittest
import time
import sys
from euler.problems.problem_2 import solve, solve_2


class SolutionTestCase(unittest.TestCase):
    condition = 4000000
    answer = 4613732

    def test_solution(self):
        self.assertEqual(solve(self.condition), self.answer)

    def test_solution_time(self):
        start_time = time.time()
        solve(self.condition)
        self.assertLess(time.time() - start_time, 60)


class Solution2TestCase(unittest.TestCase):
    condition = 4000000
    answer = 4613732

    def test_solution(self):
        self.assertEqual(solve_2(self.condition), self.answer)

    def test_solution_time(self):
        start_time = time.time()
        solve_2(self.condition)
        self.assertLess(time.time() - start_time, 60)

    def test_is_faster_solution(self):
        condition = sys.maxsize

        start_time = time.time()
        solve(condition)
        solution_1_total_time = time.time() - start_time

        start_time = time.time()
        solve_2(condition)
        solution_2_total_time = time.time() - start_time

        self.assertLess(solution_2_total_time, solution_1_total_time)


if __name__ == '__main__':
    unittest.main()
