from __future__ import annotations

import argparse
import os.path

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
    return ord(c)


def get_S_pos(s):
    for i, l in enumerate(s):
        for j, _l in enumerate(l):
            if _l == 'S':
                return (i, j)

    raise ValueError("'S' Not found")


def compute(s: str) -> int:
    s = [list(line) for line in s.splitlines()]

    pos = get_S_pos(s)
    val = get_val(s, pos)
    steps_n = 0
    visited = {pos}
    to_explore, to_explore_steps_n = [], []

    found_E = False
    while True:
        val = get_val(s, pos)
        if val == 'E':
            break
        val_value = get_ord(val)

        # Update to_explore
        possible_next_pos = []
        for move_direction in ['D', 'R', 'U', 'L']:
            _pos = move(s, pos, move_direction)
            if _pos is None:
                continue

            if _pos not in visited:
                possible_next_pos.append(_pos)

        found = False
        found_pos = None
        possible_next_pos = sorted(
            possible_next_pos,
            key=lambda x: get_ord(get_val(s, x)),
        )

        for _pos in possible_next_pos:
            _val = get_val(s, _pos)
            if _val in visited:
                continue
            _ord = get_ord(_val)
            if _ord == val_value + 1:
                if found:
                    to_explore = [_pos] + to_explore
                    to_explore_steps_n = [steps_n] + to_explore_steps_n
                    continue
                found = True
                found_pos = _pos

        for _pos in possible_next_pos:
            _val = get_val(s, _pos)
            if _val in visited:
                continue
            _ord = get_ord(_val)
            if _ord == val_value:
                if found:
                    to_explore = [_pos] + to_explore
                    to_explore_steps_n = [steps_n] + to_explore_steps_n
                    continue
                found = True
                found_pos = _pos

        for _pos in possible_next_pos:
            _val = get_val(s, _pos)
            if _val in visited:
                continue
            _ord = get_ord(_val)
            if _ord < val_value:
                if found:
                    to_explore = [_pos] + to_explore
                    to_explore_steps_n = [steps_n] + to_explore_steps_n
                    continue
                found = True
                found_pos = _pos

        if not found:
            assert to_explore
            _pos = to_explore.pop(0)
            steps_n = to_explore_steps_n.pop(0)
        else:
            _pos = found_pos

        # Start Visiting
        _steps_n = steps_n + 1
        # print(f"Visiting: FROM  {pos} ({steps_n}) -> {get_val(s, pos)} TO {_pos} ({_steps_n}) -> {get_val(s, _pos)} ")
        pos, steps_n = _pos, _steps_n
        visited.add(pos)

    return steps_n


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
