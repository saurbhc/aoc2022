from __future__ import annotations

import argparse
import os.path
import re
from typing import Any
from typing import NamedTuple

import pytest
from z3 import If
from z3 import Int
from z3 import Optimize
from z3 import sat

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

    def manhattan_distance_from_x_y(self, x: int, y: int) -> int:
        return abs(self.x - x) + abs(self.y - y)


input_r = re.compile(
    r'^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$',
)


def compute_z3(s: str, y_at_most: int = 4000000) -> int:
    o = Optimize()
    X = Int('X')
    Y = Int('Y')
    o.add(0 <= X)
    o.add(0 <= Y)
    o.add(X <= y_at_most)
    o.add(Y <= y_at_most)

    def zabs(expr: Any) -> If:
        return If(expr > 0, expr, -expr)

    for line in s.splitlines():
        result = re.search(input_r, line)
        groups = result.groups()
        sensor = Sensor(
            x=int(groups[0]),
            y=int(groups[1]),
            beacon_x=int(groups[2]),
            beacon_y=int(groups[3]),
        )

        o.add(
            (zabs(sensor.x - X) + zabs(sensor.y - Y))
            > sensor.manhattan_distance,
        )

    assert o.check() == sat
    res = o.model()

    return res[X].as_long() * 4000000 + res[Y].as_long()


def compute(s: str, y_at_most: int = 4000000) -> int:
    beacons = set()

    sensors = []
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
        sensors.append(sensor)
        beacons.add((sensor.beacon_x, sensor.beacon_y))

    for sensor in sensors:
        print(sensor, sensor.manhattan_distance)

        # top_position x should be:
        top_position = (sensor.x, sensor.y - sensor.manhattan_distance - 1)
        bottom_position = (sensor.x, sensor.y + sensor.manhattan_distance - 1)
        print(f'{top_position=} {bottom_position=}')

        expand = True
        diamond_positions = [top_position]
        while True:
            print(f'{diamond_positions=}')

            for pos in diamond_positions:
                x, y = pos
                if x < 0 or y < 0 or x > y_at_most or y > y_at_most:
                    # we don't need these
                    continue
                elif pos in beacons:
                    # remove already known beacons
                    continue

                # with all other beacons
                for _sensor in sensors:
                    if _sensor.manhattan_distance_from_x_y(x=pos[0], y=pos[1]) <= _sensor.manhattan_distance:
                        print(
                            f'{_sensor.manhattan_distance_from_x_y(pos[0], pos[1])=} <= {_sensor.manhattan_distance=}',
                        )
                        break
                    else:
                        # This is the distress beacon
                        # calculate it's tuning frequency
                        print(pos[0], pos[1])
                        return pos[0] * 4000000 + pos[1]

            if len(diamond_positions) == 1 and diamond_positions[0] == bottom_position:
                break

            if (sensor.x, sensor.y) in diamond_positions:
                expand = False

            if expand:
                diamond_positions = [(diamond_positions[0][0] - 1, diamond_positions[0][1] + 1)] + \
                    [(_pos[0], _pos[1] + 1) for _pos in diamond_positions] + \
                    [(diamond_positions[-1][0] + 1, diamond_positions[-1][1] + 1)]
            else:
                diamond_positions.pop(0)
                diamond_positions.pop()
                diamond_positions = [
                    (_pos[0], _pos[1] + 1)
                    for _pos in diamond_positions
                ]

    raise AssertionError('unreachable')


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
EXPECTED = 56000011


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute_z3(input_s, y_at_most=20) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute_z3(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
