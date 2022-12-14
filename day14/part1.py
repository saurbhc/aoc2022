from __future__ import annotations

import argparse
import os.path
from enum import Enum

import pytest

import support


INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
MAP = {}


class POSITION(Enum):
    EMPTY = 0
    SAND_AT_REST = 1
    ROCK = -1


def parse_coords(s: str) -> tuple[int, int]:
    # where x represents distance to the right
    # and y represents distance down.
    return tuple(map(int, s.split(',')))


def mark_position_as_sand(_from: tuple[int, int]) -> None:
    print(
        f'[SAND Motion] ####################################### MARKED SAND in sand_motion -> {_from=}',
    )
    if _from in MAP:
        raise AssertionError(f'marking this as sand {MAP[_from]} ')
    MAP[_from] = POSITION.SAND_AT_REST


def sand_motion(_from: tuple[int, int]) -> None:
    # How many units of sand come to rest before sand starts flowing into the abyss below?

    # A unit of sand always falls down one step if possible
    def check_coords_for_sand(
        _from,
    ): return _from in MAP and MAP[_from] == POSITION.SAND_AT_REST

    def check_coords_for_rock(
        _from,
    ): return _from in MAP and MAP[_from] == POSITION.ROCK

    print(f'[Sand Motion] starting fall {_from=}')
    keep_falling = True
    while keep_falling:
        _to = (_from[0], _from[1] + 1)
        print(f'[Sand Motion] next fall is {_from=} {_to=}')

        if check_coords_for_rock(_to) or check_coords_for_sand(_to):
            print(f'[Sand Motion] not-empty {_to=}')

            # If the tile immediately below is blocked (by rock or sand),
            # the unit of sand attempts to instead move diagonally one step down and to the left.
            # If that tile is blocked,
            # the unit of sand attempts to instead move diagonally one step down and to the right

            # try diagonally-left
            _to = (_from[0] - 1, _from[1] + 1)
            print(f'trying diagonally-left..{_from=} {_to=}')

            if check_coords_for_rock(_to) or check_coords_for_sand(_to):
                # NON-EMPTY
                # try diagonally-right
                _to = (_from[0] + 1, _from[1] + 1)
                print(f'trying diagonally-right.. {_from=} {_to=}')

                if check_coords_for_rock(_to) or check_coords_for_sand(_to):
                    # If all three possible destinations are blocked,
                    # the unit of sand comes to rest and no longer moves,
                    # at which point the next unit of sand is created back at the source.
                    print(
                        f'[Sand Motion] left & right blocked, can we put sand here? {_from=}',
                    )
                    if not check_coords_for_rock(_from) and not check_coords_for_sand(_from):
                        if check_coords_for_rock(_from):
                            return False, True
                    else:
                        print(
                            f'[Sand Motion] left & right blocked, and {_from} is NOT empty',
                        )
                        return True, True
                else:
                    # diagonally-right is empty
                    print(f'[Sand-Motion] diagonally-right is empty')
                    is_marked, wat = sand_motion(_to)
                    if wat:
                        return is_marked, wat
                    elif is_marked:
                        return True, False
                    else:
                        print(f'WTF IS GOING HERE ----------------------------')
                        continue
            else:
                # diagonally-left is empty
                print(f'[Sand-Motion] diagonally-left is empty')
                is_marked, wat = sand_motion(_to)
                if wat:
                    return is_marked, wat
                elif is_marked:
                    return True, False
                else:
                    print(f'WTF IS GOING HERE ----------------------------')
                    continue
        else:
            # Keep Falling
            print(f'[Sand Motion] Empty {_to}! Keep Falling')
            _from = _to
            continue

        if not check_coords_for_rock(_from) and not check_coords_for_sand(_from):
            print(
                f'[Sand Motion] left & right blocked, also {_from} is empty, putting sand right here {_from=}',
            )
            mark_position_as_sand(_from)
            keep_falling = False
            return True, False

    print(f'WTF IS GOING HERE (in abyss?)----------------------------')
    return False, True


def mark_position_as_rock(_from: tuple[int, int]) -> None:
    #  print(f"[Rock Motion] MARKED ROCK in rock_motion -> {_from=}")
    MAP[_from] = POSITION.ROCK


def rock_motion(_from: tuple[int, int], _to: tuple[int, int]) -> None:
    # Your scan traces the path of each solid rock structure
    # and reports the x,y coordinates that form the shape of the path,
    # where x represents distance to the right and y represents distance down

    # After the first point of each path,
    # each point indicates the end of a straight horizontal or
    # vertical line to be drawn from the previous point.

    _from, _to = parse_coords(_from), parse_coords(_to)
    #  print(f"[Rock Motion] {_from=} {_to=}")

    mark_position_as_rock(_from)

    # if same x coords
    if _from[0] == _to[0]:
        # keep falling until _to[1]
        if _to[1] > _from[1]:
            moves_n = _to[1] - _from[1]

            for _ in range(moves_n):
                _from = (_from[0], _from[1] + 1)
                mark_position_as_rock(_from)
        elif _from[1] > _to[1]:
            moves_n = _from[1] - _to[1]

            for _ in range(moves_n):
                _from = (_from[0], _from[1] - 1)
                mark_position_as_rock(_from)
        else:
            raise AssertionError(f'Are x coords equal? {_from} {_to}')
    else:
        # basically, if same y coords
        assert _from[1] == _to[1]

        if _from[0] > _to[0]:
            # move left
            moves_n = _from[0] - _to[0]

            for _ in range(moves_n):
                _from = (_from[0] - 1, _from[1])
                mark_position_as_rock(_from)
        elif _from[0] < _to[0]:
            # move right
            moves_n = _to[0] - _from[0]

            for _ in range(moves_n):
                _from = (_from[0] + 1, _from[1])
                mark_position_as_rock(_from)
        else:
            raise AssertionError(f'Are x coords equal? {_from} {_to}')


def compute(s: str) -> int:
    for path in s.splitlines():
        coords_sequence = path.split(' -> ')
        _from = coords_sequence[0]
        _to = coords_sequence[1]

        #  print(path)
        rock_motion(_from, _to)

        coords_sequence = coords_sequence[2:]
        for coord in coords_sequence:
            _from, _to = _to, coord
            rock_motion(_from, _to)

    # The sand is pouring into the cave from point 500,0.
    sand_source = parse_coords('500,0')
    sand_in_rest = 0
    falling_into_endless_void = False
    while not falling_into_endless_void:
        is_marked, falling_into_endless_void = sand_motion(sand_source)
        if is_marked:
            sand_in_rest += 1
        print(
            f'---------------------------------------------- {sand_in_rest=}',
        )


INPUT_S = '''\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''
EXPECTED = 24


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
