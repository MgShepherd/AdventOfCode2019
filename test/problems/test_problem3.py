import unittest

from aoc.problems.problem3 import Problem3
from test.test_utils import run_test_cases


class TestProblem3(unittest.TestCase):
    def test_solves_part_1(self) -> None:
        test_cases = [
            ("R8,U5,L5,D3\nU7,R6,D4,L4", 6),
            (
                "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83",
                159,
            ),
            (
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                135,
            ),
        ]
        run_test_cases(self, Problem3(), 1, test_cases)


if __name__ == "__main__":
    _ = unittest.main()
