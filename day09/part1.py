from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

HEAD = 'H'
TAIL = 'T'
DEFAULT_MAP = '''\
......
......
......
......
#.....
'''


def print_map(s: str) -> None:
    _s = ''
    for i in s:
        _s = f"{_s}{''.join(i)}\n"
    print(_s)


moves_map = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}


def compute(s: str) -> int:
    head = tail = (0, 0)
    visited = {tail}

    for line in s.splitlines():
        move, move_n = line.split(' ')
        move_n = int(move_n)

        for _ in range(move_n):
            _old_head = head
            _move = moves_map[move]
            head = (head[0] + _move[0], head[1] + _move[1])
            # print(line, head, tail)
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail = _old_head
                visited.add(tail)

    return len(visited)


INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

EXPECTED = 13


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
