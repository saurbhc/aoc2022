from __future__ import annotations

import argparse
import os.path
import re
from typing import NamedTuple

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Sensor(NamedTuple):
    x: int
    y: int
    beacon_x: int
    beacon_y: int

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x - self.beacon_x) + abs(self.y - self.beacon_y)


input_r = re.compile(
    r'^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$',
)


def compute(s: str, y: int = 2000000) -> int:
    # coords -- how many positions cannot contain a beacon
    coords = set()
    beacons = set()

    lines = s.splitlines()
    for line in lines:
        result = re.search(input_r, line)
        groups = result.groups()
        sensor = Sensor(
            x=int(groups[0]),
            y=int(groups[1]),
            beacon_x=int(groups[2]),
            beacon_y=int(groups[3]),
        )
        beacons.add((sensor.beacon_x, sensor.beacon_y))
        # print(sensor, sensor.manhattan_distance)

        # for sensor.y, the beacons should lie in the range:
        # from (sensor.x - sensor.manhattan_distance, sensor.y)
        # to (sensor.x + sensor.manhattan_distance, sensor.y)

        if y == sensor.y:
            raise NotImplementedError(f'here {y=} == {sensor.y=}')

        # if y lies upwards/downwards, it's always shrinking from sensor's pos
        # means, the positions we need to check at y are:
        # distance-from-sensor.y to y as the delta_y
        # from: (sensor.x - sensor.manhattan_distance + y, y)
        # to (sensor.x + sensor.manhattan_distance - y, y)
        delta_y = abs(sensor.y - y)
        from_position = (sensor.x - sensor.manhattan_distance + delta_y, y)
        to_position = (sensor.x + sensor.manhattan_distance - delta_y, y)
        # print(f"check from {from_position} to {to_position} | {delta_y=}")

        for pos_x in range(from_position[0], to_position[0] + 1):
            pos = (pos_x, y)
            coords.add(pos)

    coords -= beacons

    return len(coords)


INPUT_S = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
EXPECTED = 26


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s, y=10) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
