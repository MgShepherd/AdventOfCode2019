import argparse
from dataclasses import dataclass

import aoc.problems as problems
from aoc.utils.utils import print_err

SOLVED_PROBLEMS = [1, 2, 3, 4, 5, 6]


@dataclass
class ProgramArgs:
    problem: int
    part: int


def read_cmd_args() -> ProgramArgs:
    parser = argparse.ArgumentParser(
        prog="aoc", description="Solves the AdventOfCode Problems"
    )
    _ = parser.add_argument(
        "problem", type=int, choices=SOLVED_PROBLEMS, help="The problem number to solve"
    )
    _ = parser.add_argument(
        "part", type=int, choices=[1, 2], help="Which part of the problem to solve"
    )

    args = vars(parser.parse_args())
    if isinstance(args["problem"], int) and isinstance(args["part"], int):
        return ProgramArgs(int(args["problem"]), int(args["part"]))

    return ProgramArgs(1, 1)


def solve_problem(args: ProgramArgs):
    result = 0
    problem: problems.problem.Problem | None = None
    match args.problem:
        case 1:
            problem = problems.Problem1()
        case 2:
            problem = problems.Problem2()
        case 3:
            problem = problems.Problem3()
        case 4:
            problem = problems.Problem4()
        case 5:
            problem = problems.Problem5()
        case 6:
            problem = problems.Problem6()
        case _:
            print_err(f"Unsolved problem: {args.problem}")

    if problem is not None:
        result = problem.solve(args.part)
    print(f"Result is: {result}")


solve_problem(read_cmd_args())
