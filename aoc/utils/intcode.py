from dataclasses import dataclass
from enum import IntEnum


class Opcode(IntEnum):
    Add = 1
    Multiply = 2
    Input = 3
    Output = 4
    JumpIfTrue = 5
    JumpIfFalse = 6
    LessThan = 7
    Equals = 8
    Exit = 99


@dataclass
class Instruction:
    opcode: Opcode
    modes: list[int]


def run_intcode_program(elements: list[int], inputs: list[int]) -> int:
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
                    elements[elements[i + 1]] = inputs.pop(0)
                    i += 2
                case Opcode.Output:
                    outputs.append(elements[elements[i + 1]])
                    i += 2
                case Opcode.JumpIfTrue:
                    check_val = get_value(elements, i + 1, instruction.modes[0])
                    if check_val != 0:
                        new_ptr = get_value(elements, i + 2, instruction.modes[1])
                        i = new_ptr
                    else:
                        i += 3
                case Opcode.JumpIfFalse:
                    check_val = get_value(elements, i + 1, instruction.modes[0])
                    if check_val == 0:
                        new_ptr = get_value(elements, i + 2, instruction.modes[1])
                        i = new_ptr
                    else:
                        i += 3
                case Opcode.LessThan:
                    operand_1 = get_value(elements, i + 1, instruction.modes[0])
                    operand_2 = get_value(elements, i + 2, instruction.modes[1])
                    if operand_1 < operand_2:
                        elements[elements[i + 3]] = 1
                    else:
                        elements[elements[i + 3]] = 0
                    i += 4
                case Opcode.Equals:
                    operand_1 = get_value(elements, i + 1, instruction.modes[0])
                    operand_2 = get_value(elements, i + 2, instruction.modes[1])
                    if operand_1 == operand_2:
                        elements[elements[i + 3]] = 1
                    else:
                        elements[elements[i + 3]] = 0
                    i += 4
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
