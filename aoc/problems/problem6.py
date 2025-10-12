from typing import override

import aoc.utils as utils
from aoc.problems.problem import Problem
from aoc.utils.utils import print_err


class Problem6(Problem):
    @override
    def solve(self, part: int) -> int:
        file = utils.read_problem_file(6)
        if file is None:
            return 0

        direct_orbits: dict[str, list[str]] = dict()
        orbit_sources: dict[str, str] = dict()
        visited_paths: set[str] = set()
        santa_orbiting = ""
        you_orbiting = ""
        for line in file:
            elements = line.strip().split(")")
            if len(elements) != 2:
                print_err(f"Unexpected number of tokens on line {line.strip()}")

            if elements[0] in direct_orbits:
                direct_orbits[elements[0]].append(elements[1])
            else:
                direct_orbits[elements[0]] = [elements[1]]

            orbit_sources[elements[1]] = elements[0]

            if elements[1] == "YOU":
                you_orbiting = elements[0]
            elif elements[1] == "SAN":
                santa_orbiting = elements[0]

        file.close()
        if part == 1:
            return get_num_orbits(direct_orbits, "COM", 1)

        if you_orbiting == "" or santa_orbiting == "":
            print_err("Unable to find location of you or santa")
            return 0
        return get_orbital_steps(
            direct_orbits, orbit_sources, visited_paths, you_orbiting, santa_orbiting, 0
        )


def get_num_orbits(
    direct_orbits: dict[str, list[str]], current: str, level: int
) -> int:
    if current not in direct_orbits:
        return 0
    total = 0
    for element in direct_orbits[current]:
        total += level + get_num_orbits(direct_orbits, element, level + 1)

    return total


def get_orbital_steps(
    direct_orbits: dict[str, list[str]],
    orbit_sources: dict[str, str],
    visited_paths: set[str],
    current: str,
    dest: str,
    steps_taken: int,
) -> int:
    visited_paths.add(current)
    if current not in direct_orbits:
        return -1
    elif dest in direct_orbits[current]:
        return steps_taken + 1

    for element in direct_orbits[current]:
        if element in visited_paths:
            continue

        if (
            result_steps := get_orbital_steps(
                direct_orbits,
                orbit_sources,
                visited_paths,
                element,
                dest,
                steps_taken + 1,
            )
        ) != -1:
            return result_steps

    if orbit_sources[current] in visited_paths:
        return -1
    return get_orbital_steps(
        direct_orbits,
        orbit_sources,
        visited_paths,
        orbit_sources[current],
        dest,
        steps_taken + 1,
    )
