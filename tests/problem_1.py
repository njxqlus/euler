import unittest
import time
from euler.problems.problem_1 import solve


class Problem1TestCase(unittest.TestCase):
    condition = 1000
    answer = 233168

    def test_default_condition(self):
        self.assertEqual(solve(10), 23)

    def test_target_condition(self):
        self.assertEqual(solve(self.condition), self.answer)

    def test_time(self):
        start_time = time.time()
        solve(self.condition)
        self.assertLess(time.time() - start_time, 60)


if __name__ == '__main__':
    unittest.main()
