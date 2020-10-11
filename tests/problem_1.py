import unittest
import time
from euler.problems.problem_1 import problem_1


class Problem1TestCase(unittest.TestCase):
    def test_default_condition(self):
        self.assertEqual(problem_1(10), 23)

    def test_target_condition(self):
        self.assertEqual(problem_1(1000), 233168)

    def test_time(self):
        start_time = time.time()
        problem_1(1000)
        self.assertLess(time.time() - start_time, 60)


if __name__ == '__main__':
    unittest.main()
