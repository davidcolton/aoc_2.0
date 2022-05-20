import pytest
from day_06_2019 import orbits, get_visited_planets, path_to_santa


test_orbits_01 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

test_orbits_02 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
YOU)XXX
I)SAN"""


def test_visited_planets():
    i_have_orbitors, i_orbit = orbits(test_orbits_01)
    visited_planets = get_visited_planets(i_have_orbitors, i_orbit)
    assert sum(visited_planets.values()) == 42
