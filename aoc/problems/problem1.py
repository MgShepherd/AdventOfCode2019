import aoc.utils as utils


def solve():
    file = utils.read_problem_file(1)
    if file is None:
        return

    required_fuel = 0
    for line in file:
        try:
            required_fuel += int(int(line) / 3 - 2)
        except ValueError:
            utils.print_err(f"Unable to convert {line.strip()} into number")
            return

    file.close()
    print(f"Solution is {required_fuel}")
