import itertools
from typing import override

from aoc import utils
from aoc.problems.problem import Problem


class Problem7(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(7)
        if file is None:
            return 0

        data = [int(element) for element in file.read().split(",")]
        phase_options = [0, 1, 2, 3, 4]
        perms = list(itertools.permutations(phase_options))

        max_signal = 0
        for perm in perms:
            output = _get_output_signal(list(perm), data)
            if output > max_signal:
                max_signal = output
        return max_signal


def _get_output_signal(amp_inputs: list[int], program: list[int]) -> int:
    current_output = 0
    for amp_input in amp_inputs:
        inputs = [amp_input, current_output]
        current_output = utils.run_intcode_program(program.copy(), inputs)

    return current_output
