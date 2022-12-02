from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    my_points = 0
    # (1 for Rock, 2 for Paper, and 3 for Scissors)
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).

    def get_choice_score(x: str) -> int:
        if x == 'X':
            return 1
        elif x == 'Y':
            return 2
        else:
            return 3

    def get_lost_score() -> int:
        return 0

    def get_draw_score() -> int:
        return 3

    def get_win_score() -> int:
        return 6

    def is_same_choice(p1: str, p2: str) -> bool:
        if p1 == 'A' and p2 == 'X':
            return True
        elif p1 == 'B' and p2 == 'Y':
            return True
        elif p1 == 'C' and p2 == 'Z':
            return True
        else:
            return False

    def is_rock(x: str) -> bool:
        return x == 'X'

    def is_paper(x: str) -> bool:
        return x == 'Y'

    def is_scissors(x: str) -> bool:
        return x == 'Z'

    def is_rock_p1(x: str) -> bool:
        return x == 'A'

    def is_paper_p1(x: str) -> bool:
        return x == 'B'

    def is_scissors_p1(x: str) -> bool:
        return x == 'C'

    for line in lines:
        p1, p2 = line.split(' ')
        # A for Rock, B for Paper, and C for Scissors
        # X for Rock, Y for Paper, and Z for Scissors
        # Rock defeats Scissors, Scissors defeats Paper, & Paper defeats Rock.
        # If both players choose the same shape, the round ends in a draw.

        # X means you need to lose,
        # Y means you need to end the round in a draw,
        # and Z means you need to win.
        if is_rock(p2):
            # lose
            if is_rock_p1(p1):
                score = get_choice_score('Z')
            elif is_paper_p1(p1):
                score = get_choice_score('X')
            else:
                score = get_choice_score('Y')
            score += get_lost_score()
            # print(f'lose {p1=} {p2=} {score=}')
            my_points += score

        elif is_paper(p2):
            # draw
            if is_rock_p1(p1):
                score = get_choice_score('X')
            elif is_paper_p1(p1):
                score = get_choice_score('Y')
            else:
                score = get_choice_score('Z')
            score += get_draw_score()
            # print(f'lose {p1=} {p2=} {score=}')
            my_points += score

        elif is_scissors(p2):
            # win
            if is_rock_p1(p1):
                score = get_choice_score('Y')
            elif is_paper_p1(p1):
                score = get_choice_score('Z')
            else:
                score = get_choice_score('X')
            score += get_win_score()
            # print(f'win {p1=} {p2=} {score=}')
            my_points += score

    return my_points


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


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
