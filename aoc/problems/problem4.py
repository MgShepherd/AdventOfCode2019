from typing import override

from aoc.problems import Problem

PROBLEM_RANGE_START = 245318
PROBLEM_RANGE_END = 765747


class Problem4(Problem):
    @override
    def solve(self, part: int) -> int:
        num_valid = 0
        for i in range(PROBLEM_RANGE_START, PROBLEM_RANGE_END):
            if is_valid(i, part):
                num_valid += 1
        return num_valid


def is_valid(password: int, part: int) -> bool:
    digits = [int(digit) for digit in str(password)]
    has_adjacent = False
    for i in range(0, len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
        elif digits[i] == digits[i + 1] and (
            part != 2
            or (
                (i == 0 or digits[i] != digits[i - 1])
                and (i >= len(digits) - 2 or digits[i] != digits[i + 2])
            )
        ):
            has_adjacent = True

    return has_adjacent
