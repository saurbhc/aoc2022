from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    count = 0

    def is_one_fully_contains_the_other(
        _one: list[str],
        _two: list[str],
    ) -> bool:
        return int(_one[0]) <= int(_two[0]) <= int(_one[1]) and \
            int(_one[0]) <= int(_two[1]) <= int(_one[1])
    for line in lines:
        _line = line.split(',')
        one = _line[0].split('-')
        two = _line[1].split('-')
        if is_one_fully_contains_the_other(one, two) or \
                is_one_fully_contains_the_other(two, one):
            count += 1

    return count


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 2


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
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
