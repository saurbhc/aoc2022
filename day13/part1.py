from __future__ import annotations

import argparse
import json
import os.path
from typing import Any

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def check_order(l: list[Any], r: list[Any], mixed_types=False):
    for _l_i, _l in enumerate(l):

        if _l_i + 1 > len(r):
            # If the right list runs out of items first,
            # the inputs are not in the right order.
            #  print(f"> right list {r}[{_l_i+1}] runs out of order, pair not in right order")
            return False, False

        _r = r[_l_i]
        if isinstance(_l, int) and isinstance(_r, int):
            if _l == _r:
                continue
            elif _l > _r:
                #  print(f">- the inputs are not in the right order {_l} > {_r}")
                return False, False
            else:
                #  print(f">- the inputs are in the right order (left is smaller) {_l} < {_r}")
                return True, False
        else:
            if isinstance(_l, int) and isinstance(_r, list) and len(_r) == 1 and isinstance(_r[0], int):
                #  print(f"int & list {_l} {_r}")
                if _l == _r[0]:
                    continue
                elif _l > _r[0]:
                    #  print(f">- the inputs are not in the right order {_l} > {_r}")
                    return False, False
                else:
                    #  print(f">- the inputs are in the right order (left is smaller)")
                    return True, False
            elif isinstance(_l, list) and isinstance(_r, int) and len(_l) == 1 and isinstance(_l[0], int):
                #  print(f"list & int {_l} {_r}")
                if _l[0] == _r:
                    continue
                elif _l[0] > _r:
                    #  print(f">- the inputs are not in the right order {_l} > {_r}")
                    return False, False
                else:
                    #  print(f">- the inputs are in the right order (left is smaller)")
                    return True, False
            else:
                _l = [_l] if isinstance(_l, int) else _l
                _r = [_r] if isinstance(_r, int) else _r
                #  print(f"nested fn call {_l} {_r}")
                is_in_order, checked_loop = check_order(_l, _r)
                if not checked_loop:
                    return is_in_order, checked_loop
                else:
                    continue

        if _l > _r:
            # If the left integer is higher than the right integer,
            # the inputs are not in the right order
            #  print(f"> the inputs are not in the right order")
            return False, False
        elif _l < _r:
            #  print(f"> the inputs are in the right order (left is smaller)")
            return True, False

        # If the lists are the same length
        # and no comparison makes a decision about the order,
        # continue checking the next part of the input.
    else:
        # If the left list runs out of items first,
        # the inputs are in the right order.
        #  print(f"> the inputs are in the right order (for - the left list runs out of items {len(l)} {len(r)})")
        if len(l) < len(r):
            #  print(f"> break here! right order")
            return True, False
        else:
            return True, True


def compute(s: str) -> int:
    indexes = []
    pairs = []
    for index, pair in enumerate(s.split('\n\n'), start=1):
        #  print(f"=== Pair {index} ===")
        if not pair:
            continue
        #  print(f"PAIR: {pair}")
        left, right, *_ = pair.split('\n')
        left, right = json.loads(left), json.loads(right)
        is_pair_checked = False

        for l_i, l in enumerate(left):
            if l_i + 1 > len(right):
                # If the right list runs out of items first,
                # the inputs are not in the right order.
                #  print(f"right list {right}[{l_i+1}] runs out of order, not in right order.")
                break

            r = right[l_i]
            mixed_types = False
            if isinstance(l, int) and isinstance(r, int):
                # If both values are integers,
                # the lower integer should come first.

                if l < r:
                    # If the left integer is lower than the right integer,
                    # the inputs are in the right order
                    #  print(f"the inputs are in the right order {l} < {r}")
                    indexes.append(index)
                    break
                elif l > r:
                    # If the left integer is higher than the right integer,
                    # the inputs are not in the right order
                    #  print(f"the inputs are not in the right order {l} > {r}")
                    break
                else:
                    # Otherwise, the inputs are the same integer;
                    # continue checking the next part of the input.
                    #  print(f"continue checking next part of the input")
                    continue
            elif isinstance(l, int) or isinstance(r, int):
                # If exactly one value is an integer,
                # convert the integer to a list
                # which contains that integer as its only value,
                # then retry the comparison
                l = [l] if isinstance(l, int) else l
                r = [r] if isinstance(r, int) else r
                mixed_types = True

            assert isinstance(l, list)
            assert isinstance(r, list)
            #  print(l, r)
            # If both values are lists,
            # compare the first value of each list,
            # then the second value, and so on.
            is_in_order, checked_loop = check_order(l, r, mixed_types)
            if not checked_loop and is_in_order:
                #  print(">> True")
                indexes.append(index)
                break
            elif not checked_loop and not is_in_order:
                #  print(">> False")
                break

        else:
            # If the left list runs out of items first,
            # the inputs are in the right order.
            #  print(f"the inputs are in the right order (for - left list runs out of items {len(left)} {len(right)})")
            indexes.append(index)

    #  print(indexes)
    return sum(indexes)

    #          if is_pair_sorted:
    #              break
    #      else:
    #          # If the left list runs out of items first,
    #          # the inputs are in the right order.
    #          indexes.append(index)
    #
    #      left = [[l] if isinstance(l, int) else l for l in left]
    #      right = [[r] if isinstance(r, int) else r for r in right]
    #
    #      pairs.append(
    #          (left, right)
    #      )
    #
    #  indexes = []
    #  for index, (left, right) in enumerate(pairs, start=1):
    #      print(left, "---", right)
    #      is_sorted = False
    #      for l_i, l in enumerate(left):
    #          if l_i + 1 > len(right):
    #              print(f"{l_i} appending {index}")
    #              indexes.append(index)
    #              break
    #
    #          r = right[l_i]
    #
    #          for _l_i, _l in enumerate(l):
    #              if _l_i + 1 > len(r):
    #                  print(f"{_l_i} appending {index}")
    #                  indexes.append(index)
    #                  is_sorted = True
    #                  break
    #
    #              _r = r[_l_i]
    #
    #              if _l < _r:
    #                  print(index)
    #                  indexes.append(index)
    #                  is_sorted = True
    #                  break
    #          else:
    #              print(index)
    #              indexes.append(index)
    #              break
    #
    #          if is_sorted:
    #              break
    #
    #
    #  #
    #  #
    #  #      for r_i, r inrenumerate(right):
    #  #          l = left[r_i]
    #  #
    #  #          if isinstance(l, int) and isinstance(r, list):
    #  #              l = [l]
    #  #          if isinstance(r, int) and isinstance(l, list):
    #  #              r = [r]
    #  #
    #  #          if isinstance(r, list):
    #  #              for _r_i, _r in enumerate(r):
    #  #                  if _r_i+1 > len(l):
    #  #                      indexes.append(index)
    #  #                      sorted = True
    #  #                      break
    #  #                  _l = l[_r_i]
    #  #                  if _l < _r:
    #  #                      sorted = True
    #  #                      print(f"> _l < _r | {index} ")
    #  #                      indexes.append(index)
    #  #                      break
    #  #          else:
    #  #              if l < r:
    #  #                  sorted = True
    #  #                  print(f"> l < r  | {index}")
    #  #                  indexes.append(index)
    #  #                  break
    #  #      else:
    #  #          print(f"> else.....")
    #  #          indexes.append(index)
    #  #
    #  return sum(indexes)


INPUT_S = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''
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
