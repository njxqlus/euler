import time


def solution_time(self, solution, *args):
    start_time = time.time()
    solution(*args)
    self.assertLess(time.time() - start_time, 60)


def is_faster_solution(self, solution_1, solution_2, *args):
    start_time = time.time()
    solution_1(*args)
    solution_1_total_time = time.time() - start_time

    start_time = time.time()
    solution_2(*args)
    solution_2_total_time = time.time() - start_time

    self.assertLess(solution_2_total_time, solution_1_total_time)
