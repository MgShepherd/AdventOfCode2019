from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem


class Problem1(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(1)

        if file is None:
            return -1

        required_fuel = 0
        for line in file:
            try:
                required_fuel += self._get_required_fuel(part, int(line))
            except ValueError:
                utils.print_err(f"Unable to convert {line.strip()} into number")
                return -1

        file.close()
        return required_fuel

    def _get_required_fuel(self, part: int, mass: int) -> int:
        required_fuel = int(mass / 3) - 2
        if part == 1:
            return required_fuel
        elif required_fuel <= 0:
            return 0
        return required_fuel + self._get_required_fuel(part, required_fuel)
