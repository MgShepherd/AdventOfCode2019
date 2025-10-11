from enum import IntEnum
from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem

JUMP_AMOUNT = 4
PART_2_TARGET_VALUE = 19690720


class Opcode(IntEnum):
    Add = 1
    Multiply = 2
    Exit = 99


class Problem2(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(2)
        if file is None:
            return -1

        data = file.readline().strip().split(",")
        elements = list(map(lambda x: int(x), data))

        if part == 1:
            return _run_program(elements)
        elif part == 2:
            return _run_part_2(elements)
        return 0


def _run_program(elements: list[int]) -> int:
    for i in range(0, len(elements), JUMP_AMOUNT):
        try:
            match Opcode(elements[i]):
                case Opcode.Add:
                    elements[elements[i + 3]] = (
                        elements[elements[i + 1]] + elements[elements[i + 2]]
                    )
                case Opcode.Multiply:
                    elements[elements[i + 3]] = (
                        elements[elements[i + 1]] * elements[elements[i + 2]]
                    )
                case Opcode.Exit:
                    break
        except ValueError:
            print(f"Unable to process opcode {elements[i]}")
            break
        except IndexError:
            print(f"Reached an index outside of range of the array: {i}")
            break

    return elements[0]


def _run_part_2(initial_config: list[int]) -> int:
    for noun in range(0, 99):
        for verb in range(0, 99):
            elements = initial_config.copy()
            elements[1] = noun
            elements[2] = verb
            if _run_program(elements) == PART_2_TARGET_VALUE:
                return 100 * noun + verb
            del elements
    return 0
