from aoc.data import read_data as rd
from collections import defaultdict

from typing import Tuple


def path_to_com(i_orbit: dict, name: str) -> list:
    path_to_com = [name]
    planet = i_orbit[name]
    while planet != "COM":
        path_to_com.append(planet)
        planet = i_orbit[planet]
    path_to_com.append("COM")

    return path_to_com


def orbits(orbit_map: str) -> Tuple[defaultdict, dict]:

    orbit_tuples = [(x[0], x[1]) for x in [y.split(")") for y in orbit_map.split()]]

    i_have_orbitors = defaultdict(list)
    i_orbit = dict()

    for p, o in orbit_tuples:
        i_have_orbitors[p].append(o)

    for key, values in i_have_orbitors.items():
        for value in values:
            # print(value, key)
            i_orbit[value] = key

    return i_have_orbitors, i_orbit


def get_visited_planets(i_have_orbitors: defaultdict, i_orbit: dict) -> dict:

    visited_planets = dict()
    planets_to_visit = i_have_orbitors["COM"]
    visited_planets["COM"] = 0

    while len(planets_to_visit) != 0:
        # print(f"Planets to visit: {planets_to_visit}")

        visiting = planets_to_visit.pop(0)
        # print(f"Currently visiting: {visiting} and I orbit {i_orbit[visiting]}")

        if visiting in i_have_orbitors.keys():
            planets_to_visit.extend(i_have_orbitors[visiting])
        if i_orbit[visiting] in visited_planets.keys():
            visited_planets[visiting] = visited_planets[i_orbit[visiting]] + 1

    return visited_planets


def path_to_santa(
    i_have_orbitors: defaultdict,
    i_orbit: dict,
    visited_planets: dict,
) -> int:

    # Get full paths to COM
    you_path = path_to_com(i_orbit, "YOU")
    san_path = path_to_com(i_orbit, "SAN")

    # Reverse paths to com
    you_path = you_path[::-1]
    san_path = san_path[::-1]

    first_different = min(
        [index for index, elem in enumerate(you_path) if elem != san_path[index]]
    )

    # print(you_path[first_different - 1], san_path[first_different - 1])
    # print(you_path[first_different], san_path[first_different])

    you_steps_to_com = visited_planets["YOU"]
    san_steps_to_com = visited_planets["SAN"]
    common_steps_to_com = visited_planets[you_path[first_different - 1]]

    you_to_san = (you_steps_to_com - 1 + san_steps_to_com - 1) - (
        common_steps_to_com * 2
    )

    return you_to_san


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_06.txt"
    raw_data = rd(input)

    i_have_orbitors, i_orbit = orbits(raw_data)
    visited_planets = get_visited_planets(i_have_orbitors, i_orbit)
    you_to_santa = path_to_santa(i_have_orbitors, i_orbit, visited_planets)

    print(f"PART 01: {sum(visited_planets.values())}")
    print(f"PART 02: {you_to_santa}")
