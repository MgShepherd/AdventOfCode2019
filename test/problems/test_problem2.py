import unittest

from aoc.problems import Problem2
from test.test_utils import run_test_cases


class TestProblem2(unittest.TestCase):
    def test_solves_part_1(self) -> None:
        test_cases = [
            ("1,9,10,3,2,3,11,0,99,30,40,50", 3500),
            ("1,1,1,4,99,5,6,0,99", 30),
        ]
        run_test_cases(self, Problem2(), 1, test_cases)

    def test_solves_part_2(self) -> None:
        print("Tests N/A for problem 2 part 1 due to no examples")


if __name__ == "__main__":
    _ = unittest.main()
