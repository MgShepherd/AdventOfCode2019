from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem
from aoc.utils.utils import print_err


class Problem6(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(6)
        if file is None:
            return 0

        direct_orbits: dict[str, list[str]] = dict()
        for line in file:
            elements = line.strip().split(")")
            if len(elements) != 2:
                print_err(f"Unexpected number of tokens on line {line.strip()}")

            if elements[0] in direct_orbits:
                direct_orbits[elements[0]].append(elements[1])
            else:
                direct_orbits[elements[0]] = [elements[1]]

        file.close()
        return get_num_orbits(direct_orbits, "COM", 1)


def get_num_orbits(
    direct_orbits: dict[str, list[str]], current: str, level: int
) -> int:
    if current not in direct_orbits:
        return 0
    total = 0
    for element in direct_orbits[current]:
        total += level + get_num_orbits(direct_orbits, element, level + 1)

    return total
