from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def get_t_scenic_score(t, left, right, top, bottom):
    # print(t, left, right, top, bottom)
    scenic_score1 = 0
    for i in list(reversed(left)):
        scenic_score1 += 1
        if i >= t:
            break

    scenic_score2 = 0
    for i in right:
        scenic_score2 += 1
        if i >= t:
            break

    scenic_score3 = 0
    for i in list(reversed(top)):
        scenic_score3 += 1
        if i >= t:
            break

    scenic_score4 = 0
    for i in bottom:
        scenic_score4 += 1
        if i >= t:
            break

    scenic_score1 = scenic_score1 or 1
    scenic_score2 = scenic_score2 or 1
    scenic_score3 = scenic_score3 or 1
    scenic_score4 = scenic_score4 or 1
    # print(scenic_score1, scenic_score2, scenic_score3, scenic_score4)
    return scenic_score1 * scenic_score2 * scenic_score3 * scenic_score4


def compute(s: str) -> int:
    trees_map = [list(line) for line in s.splitlines()]
    c_n, _ = len(trees_map[0]), len(trees_map)
    max_scenic_score = 0
    for idx, tree_line in enumerate(trees_map):
        if idx in [0, len(trees_map)-1]:
            # edge tree (top/bottom edge)
            # print("------------", idx, tree_line)
            # visible_n += len(trees_map)
            continue

        for _idx, t in enumerate(tree_line):
            if _idx in [0, len(tree_line)-1]:
                # edge tree (left/right edge)
                # print("------------", _idx, t)
                # visible_n += 1
                continue

            scenic_score = get_t_scenic_score(
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
            # print(f"{scenic_score=} {t}")
            if scenic_score > max_scenic_score:
                # visible_n += 1
                max_scenic_score = scenic_score

    return max_scenic_score


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 8


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
