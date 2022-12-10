from __future__ import annotations

import argparse
import os.path
from collections import deque
from itertools import islice

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


def apply_move(head, move):
    return (
        head[0] + move[0],
        head[1] + move[1],
    )


def get_updated_tail(head, tail, old_head):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        return old_head, True

    return tail, False


def update_location(current_head_i, current_tail_i, current_positions):
    head_x, head_y = current_positions[current_head_i]
    tail_x, tail_y = current_positions[current_tail_i]

    x_diff = head_x - tail_x
    y_diff = head_y - tail_y

    if abs(y_diff) == 2 and abs(x_diff) == 2:
        return ((head_x + tail_x) // 2, (head_y + tail_y) // 2)
    if abs(y_diff) == 2:
        return (head_x, (tail_y + head_y) // 2)
    elif abs(x_diff) == 2:
        return ((tail_x + head_x) // 2, head_y)
    else:
        return (tail_x, tail_y)

    # if x_diff > 1:
    #     tail_x = head_x - 1
    #     tail_y = head_y
    # elif x_diff < -1:
    #     tail_x = head_x + 1
    #     tail_y = head_y
    # elif y_diff > 1:
    #     tail_x = head_x
    #     tail_y = head_y - 1  # if x_diff > 1 or y_diff > 1:
    # elif y_diff < -1:
    #     tail_x = head_x
    #     tail_y = head_y + 1#     # not touching

    current_positions[current_tail_i] = (tail_x, tail_y)

    return current_positions


def compute(s: str) -> int:
    head = (0, 0)
    current_positions = [head for _ in range(10)]
    visited = {head}

    for line in s.splitlines():
        move, move_n = line.split(' ')
        move_n = int(move_n)

        for _ in range(move_n):

            current_positions[0] = apply_move(
                current_positions[0], moves_map[move],
            )

            for i in range(1, 10):
                current_positions[i] = update_location(
                    current_head_i=i-1,
                    current_tail_i=i,
                    current_positions=current_positions,
                )
            visited.add(current_positions[9])

    return len(visited)


INPUT_S = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''

EXPECTED = 36

INPUT_S2 = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

EXPECTED2 = 1


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
        (INPUT_S2, EXPECTED2),
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
