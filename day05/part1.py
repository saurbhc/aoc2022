from __future__ import annotations

import argparse
import os.path
import re

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    _stacks, moves = s.split('\n\n')
    length = len(_stacks.splitlines()[0])
    stacks = [[] for x in range(0, length, 4)]

    # temp_top_stack = stacks.splitlines()[0]
    # temp_top_stack[0:3]
    # temp_top_stack[4:7]
    # temp_top_stack[8:11]
    # temp_top_stack[12:15]

    for index, line in enumerate(_stacks.splitlines()):
        for _index, i in enumerate(range(0, length, 4)):
            value = line[i:i+3][1].strip()
            if value.isdigit():
                continue
            if not value:
                continue
            stack_index_list = stacks[_index]
            stack_index_list = [value] + stack_index_list
            stacks[_index] = stack_index_list

    for move in moves.splitlines():
        crate_n, from_idx, to_idx = re.findall(r'\d+', move)
        crate_n, from_idx, to_idx = int(crate_n), int(from_idx), int(to_idx)

        # index starts from 0
        from_idx -= 1
        to_idx -= 1

        stacks[to_idx] += list(reversed(stacks[from_idx][-crate_n:]))
        stacks[from_idx] = stacks[from_idx][:-crate_n]

    end = ''
    for i in stacks:
        end += i[-1]
    return end


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'CMZ'


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
