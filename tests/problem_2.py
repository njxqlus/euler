import unittest
import time
from euler.problems.problem_2 import problem_2


class Problem2TestCase(unittest.TestCase):
    def test_default_condition(self):
        self.assertEqual(problem_2(4000000), 4613732)

    def test_time(self):
        start_time = time.time()
        problem_2(1000)
        self.assertLess(time.time() - start_time, 60)


if __name__ == '__main__':
    unittest.main()
