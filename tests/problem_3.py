import unittest
import time
from euler.problems.problem_3 import is_prime, solve, solve_2


class SolutionTestCase(unittest.TestCase):
    condition = 600851475143
    answer = 6857

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(40))

    def test_solution_with_default_condition(self):
        self.assertEqual(29, solve(13195))

    def test_solution(self):
        self.assertEqual(self.answer, solve(self.condition))

    def test_solution_time(self):
        start_time = time.time()
        solve(self.condition)
        self.assertLess(time.time() - start_time, 60)


class Solution2TestCase(unittest.TestCase):
    condition = 600851475143
    answer = 6857

    def test_solution(self):
        self.assertEqual(self.answer, solve_2(self.condition))

    def test_is_faster_solution(self):
        start_time = time.time()
        solve(self.condition)
        solution_1_total_time = time.time() - start_time

        start_time = time.time()
        solve_2(self.condition)
        solution_2_total_time = time.time() - start_time

        self.assertLess(solution_2_total_time, solution_1_total_time)


if __name__ == '__main__':
    unittest.main()
