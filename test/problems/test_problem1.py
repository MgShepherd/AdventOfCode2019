import unittest

from aoc.problems import Problem1
from test.test_utils import run_test_cases


class TestProblem1(unittest.TestCase):
    def test_solves_part_1(self) -> None:
        test_cases = [("12", 2), ("100756", 33583), ("14\n1969", 656)]
        run_test_cases(self, Problem1(), 1, test_cases)

    def test_solves_part_2(self) -> None:
        test_cases = [("14", 2), ("1969", 966), ("100756", 50346)]
        run_test_cases(self, Problem1(), 2, test_cases)


if __name__ == "__main__":
    _ = unittest.main()
