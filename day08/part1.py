from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def is_t_visible(t, left, right, top, bottom):
    # print(t, left, right, top, bottom)
    for i in left:
        if i >= t:
            # not visible here
            break
    else:
        # print(left)
        return True

    for i in right:
        if i >= t:
            # not visible here
            break
    else:
        # print(right)
        return True

    for i in top:
        if i >= t:
            # not visible here
            break
    else:
        # print(top)
        return True

    for i in bottom:
        if i >= t:
            # not visible here
            break
    else:
        # print(bottom)
        return True

    return False


def compute(s: str) -> int:
    trees_map = [list(line) for line in s.splitlines()]
    c_n, _ = len(trees_map[0]), len(trees_map)
    visible_n = 0
    for idx, tree_line in enumerate(trees_map):
        if idx in [0, len(trees_map)-1]:
            # edge tree (top/bottom edge)
            # print("------------", idx, tree_line)
            visible_n += len(trees_map)
            continue

        for _idx, t in enumerate(tree_line):
            if _idx in [0, len(tree_line)-1]:
                # edge tree (left/right edge)
                # print("------------", _idx, t)
                visible_n += 1
                continue

            is_visible = is_t_visible(
                int(t),
                left=[int(i) for i in tree_line[:_idx]],
                right=[int(i) for i in tree_line[_idx+1:]],
                top=[
                    int(trees_map[i_c_n][_idx])
                    for i_c_n in range(c_n) if i_c_n < idx
                ],
                bottom=[
                    int(trees_map[i_c_n][_idx])
                    for i_c_n in range(c_n) if i_c_n > idx
                ],
            )
            if is_visible:
                visible_n += 1
                # print(is_visible)

    return visible_n


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 21


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
