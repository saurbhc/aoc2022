from __future__ import annotations

import argparse
import copy
import json
import math
import os.path
from collections import defaultdict
from typing import Any

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

MONKEY_ITEMS = defaultdict(list)
MONKEY_ITEMS_N = defaultdict(int)
MONKEY_INFO = defaultdict(dict)

MONKEY_SUPER_MODULO = None


def inspect_item_by_monkey_m(monkey_n: int, monkey_item: int) -> int:
    monkey_info = MONKEY_INFO[monkey_n]
    old = monkey_item
    expression1 = monkey_info['expression1']
    old %= MONKEY_SUPER_MODULO
    expression_test = monkey_info['expression_test']

    old = eval(monkey_info['expression1'])
    is_test_passed = eval(monkey_info['expression_test'])

    throw_to_monkey_m = monkey_info['true'] if is_test_passed else monkey_info['false']

    return throw_to_monkey_m, old


def compute(s: str) -> int:
    for m_info in s.split('\n\n'):
        lines = m_info.splitlines()
        monkey_n = None

        for line in lines:
            if not monkey_n and line.startswith('Monkey'):
                monkey_n = int(line[-2])
                continue

            # check the current monkey inspection task
            key, value = line.split(': ')
            key = key.strip()
            if key == 'Starting items':
                value = value.split(', ')
                MONKEY_ITEMS[monkey_n].extend(
                    [int(i.strip()) for i in value],
                )
            elif key == 'Operation':
                expression = value.split('new = ')[-1]
                MONKEY_INFO[monkey_n]['expression1'] = expression
            elif key == 'Test':
                _, div_n = value.split('divisible by ')
                MONKEY_INFO[monkey_n]['expression_test'] = f'old % {div_n} == 0'
                MONKEY_INFO[monkey_n]['div_by'] = div_n
            elif key.startswith('If'):
                _, throw_m_n = value.split('throw to monkey ')
                if key.split(' ')[-1] == 'true':
                    MONKEY_INFO[monkey_n]['true'] = int(throw_m_n)
                else:
                    MONKEY_INFO[monkey_n]['false'] = int(throw_m_n)
            else:
                raise NotImplementedError(line)

    for round_n in range(1, 10001):
        for monkey_n in MONKEY_ITEMS.keys():
            global MONKEY_SUPER_MODULO
            if MONKEY_SUPER_MODULO is None:
                mods = [
                    int(i['div_by'])
                    for _, i in MONKEY_INFO.items()
                ]

                MONKEY_SUPER_MODULO = math.prod(mods)
            for monkey_item in MONKEY_ITEMS[monkey_n]:
                throw_to_monkey_m, worry_level = inspect_item_by_monkey_m(
                    monkey_n,
                    monkey_item,
                )

                # Remove current item
                MONKEY_ITEMS[monkey_n] = MONKEY_ITEMS[monkey_n][1:]
                # Update count of items inspected by monkey_n
                MONKEY_ITEMS_N[monkey_n] += 1
                # Throw item to another monkey
                MONKEY_ITEMS[throw_to_monkey_m].append(worry_level)
        # print(round_n, MONKEY_ITEMS)

    top_two_most_avtive_monkeys = sorted(
        list(MONKEY_ITEMS_N.values()), reverse=True,
    )

    return top_two_most_avtive_monkeys[0] * top_two_most_avtive_monkeys[1]


INPUT_S = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''
EXPECTED = 2713310158


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
