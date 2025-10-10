from enum import IntEnum
from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem

JUMP_AMOUNT = 4


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

        return elements[0]
