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
        visted_locations: dict[Point, int] = dict()
        crossed_locations: dict[Point, int] = dict()
        current_location = Point(0, 0)
        current_distance = 0

        for movement in path1.strip().split(","):
            current_location, current_distance = _process_movement(
                movement,
                current_location,
                current_distance,
                visted_locations,
                crossed_locations,
                True,
            )

        current_location = Point(0, 0)
        current_distance = 0
        for movement in path2.strip().split(","):
            current_location, current_distance = _process_movement(
                movement,
                current_location,
                current_distance,
                visted_locations,
                crossed_locations,
                False,
            )

        if part == 1:
            return get_min_crossed_distance(crossed_locations)

        return get_min_crossed_steps(crossed_locations, visted_locations)


def _process_movement(
    movement: str,
    current_location: Point,
    current_distance: int,
    visted_locations: dict[Point, int],
    crossed_locations: dict[Point, int],
    first_visit: bool,
) -> tuple[Point, int]:
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
            current_distance += 1

            if first_visit and current_location not in visted_locations:
                visted_locations[current_location] = current_distance
            elif (
                not first_visit
                and current_location in visted_locations
                and current_location not in crossed_locations
            ):
                crossed_locations[current_location] = current_distance
    except ValueError:
        print_err(f"Unable to process movement element {movement}")

    return current_location, current_distance


def get_min_crossed_distance(crossed_locations: dict[Point, int]) -> int:
    min_dist = -1
    for loc in crossed_locations:
        if min_dist == -1 or abs(loc.x) + abs(loc.y) < min_dist:
            min_dist = abs(loc.x) + abs(loc.y)

    return min_dist


def get_min_crossed_steps(
    crossed_locations: dict[Point, int], visted_locations: dict[Point, int]
) -> int:
    min_steps = -1
    for loc in crossed_locations:
        if (
            min_steps == -1
            or crossed_locations[loc] + visted_locations[loc] < min_steps
        ):
            min_steps = crossed_locations[loc] + visted_locations[loc]
    return min_steps
