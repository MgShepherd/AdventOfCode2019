from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem
from aoc.utils.intcode import run_intcode_program


class Problem5(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(5)
        if file is None:
            return -1

        data = file.readline().strip().split(",")
        elements = list(map(lambda x: int(x), data))

        if part == 1:
            return run_intcode_program(elements, [1])
        return run_intcode_program(elements, [5])
