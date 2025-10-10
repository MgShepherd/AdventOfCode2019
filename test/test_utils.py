import io
import unittest
from unittest.mock import patch

from aoc import problems


def run_test_cases(
    test_runner: unittest.TestCase,
    problem: problems.Problem,
    part: int,
    test_cases: list[tuple[str, int]],
):
    for input, expected in test_cases:
        with test_runner.subTest(p1=input, p2=expected):
            with patch("aoc.utils.read_problem_file", return_value=io.StringIO(input)):
                test_runner.assertEqual(problem.solve(part), expected)
