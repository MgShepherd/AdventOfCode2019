import io
import unittest
from unittest.mock import patch

from aoc.problems import problem1


class TestProblem1(unittest.TestCase):
    def test_solves_part_1(self) -> None:
        test_cases = [("12", 2), ("100756", 33583), ("14\n1969", 656)]
        for input, expected in test_cases:
            with self.subTest(p1=input, p2=expected):
                with patch(
                    "aoc.utils.read_problem_file", return_value=io.StringIO(input)
                ):
                    self.assertEqual(problem1.solve(1), expected)

    def test_solves_part_2(self) -> None:
        test_cases = [("14", 2), ("1969", 966), ("100756", 50346)]
        for input, expected in test_cases:
            with self.subTest(p1=input, p2=expected):
                with patch(
                    "aoc.utils.read_problem_file", return_value=io.StringIO(input)
                ):
                    self.assertEqual(problem1.solve(2), expected)


if __name__ == "__main__":
    _ = unittest.main()
