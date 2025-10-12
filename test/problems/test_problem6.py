import unittest

from aoc.problems.problem6 import Problem6
from test.test_utils import run_test_cases


class TestProblem6(unittest.TestCase):
    def test_solves_part_1(self) -> None:
        test_cases = [
            (
                """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""",
                42,
            ),
        ]
        run_test_cases(self, Problem6(), 1, test_cases)

    def test_solves_part_2(self) -> None:
        test_cases = [
            (
                """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""",
                4,
            ),
        ]
        run_test_cases(self, Problem6(), 2, test_cases)


if __name__ == "__main__":
    _ = unittest.main()
