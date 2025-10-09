import sys
from typing import IO, Any


def print_err(msg):
    print(f"\033[31m[ERROR]: {msg}\033[0m", file=sys.stderr)


def read_problem_file(problem_number: int) -> IO[Any]:
    file_name = f"inputs/problem{problem_number}.txt"
    try:
        return open(file_name)
    except FileNotFoundError:
        print_err(f"Unable to read file {file_name}")
        return None
    except Exception as e:
        print_err(f"There was a problem reading the problem input {e}")
        return None
