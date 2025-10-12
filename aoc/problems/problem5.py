from dataclasses import dataclass
from enum import IntEnum
from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem

JUMP_AMOUNT = 4
INPUT_VAL = 1


class Opcode(IntEnum):
    Add = 1
    Multiply = 2
    Input = 3
    Output = 4
    Exit = 99


@dataclass
class Instruction:
    opcode: Opcode
    modes: list[int]


class Problem5(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(5)
        if file is None:
            return -1

        data = file.readline().strip().split(",")
        elements = list(map(lambda x: int(x), data))

        return _run_program(elements)


def _run_program(elements: list[int]) -> int:
    i = 0
    outputs: list[int] = []
    while i < len(elements):
        try:
            instruction = _parse_instruction(str(elements[i]))
            match instruction.opcode:
                case Opcode.Add:
                    operand_1 = get_value(elements, i + 1, instruction.modes[0])
                    operand_2 = get_value(elements, i + 2, instruction.modes[1])
                    elements[elements[i + 3]] = operand_1 + operand_2
                    i += 4
                case Opcode.Multiply:
                    operand_1 = get_value(elements, i + 1, instruction.modes[0])
                    operand_2 = get_value(elements, i + 2, instruction.modes[1])
                    elements[elements[i + 3]] = operand_1 * operand_2
                    i += 4
                case Opcode.Input:
                    elements[elements[i + 1]] = INPUT_VAL
                    i += 2
                case Opcode.Output:
                    outputs.append(elements[elements[i + 1]])
                    i += 2
                case Opcode.Exit:
                    break
        except ValueError:
            print(f"Unable to process opcode {elements[i]}")
            break
        except IndexError:
            print(f"Reached an index outside of range of the array: {i}")
            break

    return outputs[len(outputs) - 1]


def _parse_instruction(element: str) -> Instruction:
    instruction_modes = [0, 0, 0]
    opcode = Opcode(int(element[len(element) - 2 :]))
    for i in range(len(element) - 3, -1, -1):
        instruction_modes[len(element) - 3 - i] = int(element[i])
    return Instruction(opcode, instruction_modes)


def get_value(elements: list[int], index: int, instruction_mode: int) -> int:
    if instruction_mode == 0:
        return elements[elements[index]]
    return elements[index]
