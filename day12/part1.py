from __future__ import annotations

import argparse
import os.path
from collections import deque

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


MOVE = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}


def move(s: list[list[str]], pos: tuple[int], move_direction: str):
    _move = MOVE[move_direction]
    # print(f"----- {pos} + {_move}")
    pos = (pos[0] + _move[0], pos[1] + _move[1])
    # print(f"new pos {pos}")

    # is pos reachable
    if 0 <= pos[0] <= len(s) - 1 and 0 <= pos[1] <= len(s[0]) - 1:
        return pos
    else:
        return None


def get_val(s: list[list[str]], pos: tuple[int]):
    return s[pos[0]][pos[1]]


def get_ord(c: str) -> int:
    if c == 'S':
        return 96
    elif c == 'E':
        return 123
    return ord(c)


def get_S_pos(s):
    for i, l in enumerate(s):
        for j, _l in enumerate(l):
            if _l == 'S':
                return (i, j)

    raise ValueError("'S' Not found")


def get_E_pos(s):
    for i, l in enumerate(s):
        for j, _l in enumerate(l):
            if _l == 'E':
                return (i, j)

    raise ValueError("'E' Not found")


def compute(s: str) -> int:
    s = [list(line) for line in s.splitlines()]
    s_adj = {}
    for i, line in enumerate(s):
        for j, val_s in enumerate(line):
            # find all possible_next_pos for val_s
            pos = (i, j)
            ord_s = get_ord(val_s)

            possible_next_pos = []
            for move_direction in ['U', 'D', 'L', 'R']:
                _pos = move(s, pos, move_direction)
                if _pos is None:
                    continue

                _val = get_val(s, _pos)
                _ord = get_ord(_val)
                if ord_s+1 >= _ord:
                    possible_next_pos.append(_pos)

            s_adj[pos] = possible_next_pos

    S_pos = get_S_pos(s)
    E_pos = get_E_pos(s)
    EXPLORING_QUEUE = deque(
        [(S_pos, 0)],
    )

    VISITED_SET = {S_pos}
    while EXPLORING_QUEUE:
        first = EXPLORING_QUEUE.popleft()
        current_pos = first[0]
        current_pos_steps = first[1]

        if current_pos == E_pos:
            return current_pos_steps

        current_pos_adj = s_adj[current_pos]
        for _current_pos_adj in current_pos_adj:
            if _current_pos_adj in VISITED_SET:
                continue

            VISITED_SET.add(
                _current_pos_adj,
            )
            EXPLORING_QUEUE.append(
                (_current_pos_adj, current_pos_steps+1),
            )

        EXPLORING_QUEUE = deque(
            sorted(
                EXPLORING_QUEUE,
                key=lambda x: x[-1],
            ),
        )

    raise AssertionError('wat')


INPUT_S = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
EXPECTED = 31


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
