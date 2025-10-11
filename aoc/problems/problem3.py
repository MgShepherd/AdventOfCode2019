from dataclasses import dataclass
from typing import override

from aoc import utils
from aoc.problems import Problem
from aoc.utils.utils import print_err


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class Problem3(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(3)
        if file is None:
            return 0

        path1 = file.readline()
        path2 = file.readline()
        visted_locations: set[Point] = set()
        crossed_locations: set[Point] = set()
        current_location = Point(0, 0)

        for movement in path1.strip().split(","):
            current_location = _process_movement(
                movement, current_location, visted_locations, crossed_locations, True
            )

        current_location = Point(0, 0)
        for movement in path2.strip().split(","):
            current_location = _process_movement(
                movement, current_location, visted_locations, crossed_locations, False
            )

        return get_min_crossed_distance(crossed_locations)


def _process_movement(
    movement: str,
    current_location: Point,
    visted_locations: set[Point],
    crossed_locations: set[Point],
    first_visit: bool,
) -> Point:
    try:
        amount = int(movement[1:])
        for _ in range(1, amount + 1):
            match movement[0]:
                case "U":
                    current_location = Point(current_location.x, current_location.y + 1)
                case "D":
                    current_location = Point(current_location.x, current_location.y - 1)
                case "L":
                    current_location = Point(current_location.x - 1, current_location.y)
                case "R":
                    current_location = Point(current_location.x + 1, current_location.y)
                case _:
                    print_err(f"Unexpected movement direction: {movement[0]}")

            if first_visit:
                visted_locations.add(current_location)
            elif current_location in visted_locations:
                crossed_locations.add(current_location)
    except ValueError:
        print_err(f"Unable to process movement element {movement}")

    return current_location


def get_min_crossed_distance(crossed_locations: set[Point]) -> int:
    min_dist = -1
    for loc in crossed_locations:
        if min_dist == -1 or abs(loc.x) + abs(loc.y) < min_dist:
            min_dist = abs(loc.x) + abs(loc.y)
    return min_dist
