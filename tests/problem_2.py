import unittest
import time
from euler.problems.problem_2 import solve


class Problem2TestCase(unittest.TestCase):
    condition = 4000000
    answer = 4613732

    def test_default_condition(self):
        self.assertEqual(solve(self.condition), self.answer)

    def test_time(self):
        start_time = time.time()
        solve(self.condition)
        self.assertLess(time.time() - start_time, 60)


if __name__ == '__main__':
    unittest.main()
