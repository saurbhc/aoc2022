from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    marker_n = 14
    markers: list[str] = []
    for idx, i in enumerate(s):
        if len(markers) != marker_n:
            markers.append(i)
            continue

        if len(set(markers)) == marker_n:
            return idx

        markers.pop(0)
        markers.append(i)

    return idx


INPUT_S = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
EXPECTED = 23

INPUT_S2 = 'nppdvjthqldpwncqszvftbrmjlhg'
EXPECTED2 = 23

INPUT_S3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
EXPECTED3 = 29

INPUT_S4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
EXPECTED4 = 26

INPUT_S0 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
EXPECTED0 = 19


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
        (INPUT_S2, EXPECTED2),
        (INPUT_S3, EXPECTED3),
        (INPUT_S4, EXPECTED4),
        (INPUT_S0, EXPECTED0),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
