# generate maps
from __future__ import annotations
default_map = '''\
....
....
....
....
'''

HEAD = 'H'
TAIL = 'T'


def generate_maps() -> list[str]:
    maps = []
    for i in range(4):
        # row

        for j in range(4):
            # column

            # add TAIL
            # left
            _t = j - 1
            if _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[i][_t] = TAIL
                pass  # print('left: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # right
            _t = j + 1
            if _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[i][_t] = TAIL
                pass  # print('right: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # top
            _i = i - 1
            _t = j
            if _i in range(4) and _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[_i][_t] = TAIL
                pass  # print('top: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # bottom
            _i = i + 1
            _t = j
            if _i in range(4) and _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[_i][_t] = TAIL
                pass  # print('bottom: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # top-diagonally-left
            _i = i - 1
            _t = j - 1
            if _i in range(4) and _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[_i][_t] = TAIL
                pass  # print('top-diagonally-left: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # top-diagonally-right
            _i = i - 1
            _t = j + 1
            if _i in range(4) and _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[_i][_t] = TAIL
                pass  # print('top-diagonally-right: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # bottom-diagonally-left
            _i = i + 1
            _t = j - 1
            if _i in range(4) and _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[_i][_t] = TAIL
                pass  # print('bottom-diagonally-left: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

            # bottom-diagonally-right
            _i = i + 1
            _t = j + 1
            if _i in range(4) and _t in range(4):
                # add HEAD
                s = [list(i) for i in default_map.splitlines()]
                s[i][j] = HEAD
                s[_i][_t] = TAIL
                pass  # print('bottom-diagonally-right: ')
                maps.append(s)
                for l in s:
                    pass  # print(''.join(l))

    return maps


def verify_final_map(s: str) -> bool:
    pass  # print(f"Map: \n{s}")
    # _map = [list(line) for line in s.splitlines()]
    _map = s

    for idx, line in enumerate(_map):
        if HEAD in line:
            h_i = line.index(HEAD)
            h_line_i = idx
            break
    else:
        raise ValueError(f'can\t find {HEAD}')

    # if 'T' is not in map, then it's at the same place of 'H'
    if TAIL not in s:
        pass  # print(f"{TAIL} is at the same location of {HEAD}")
        return True

    # 'T' should be either up/down/left/right or in diagonal
    pass  # print(f"{h_i=} {h_line_i=}")

    t_left_i = h_i - 1
    pass  # print(f"checking left {t_left_i=} on line {h_line_i=}")
    if t_left_i in range(len(_map[0])):
        if _map[h_line_i][t_left_i] == TAIL:
            pass  # print(f"{TAIL} is on the left of {HEAD}")
            return True
    else:
        pass  # print(f"{t_left_i} not in {range(len(_map[0]))}")

    t_right_i = h_i + 1
    pass  # print(f"checking right {t_right_i=} on line {h_line_i=}")
    if t_right_i in range(len(_map[0])):
        if _map[h_line_i][t_right_i] == TAIL:
            pass  # print(f"{TAIL} is on the right of {HEAD}")
            return True
    else:
        pass  # print(f"{t_right_i} not in {range(len(_map[0]))}")

    t_top_i = h_i
    _h_line_i = h_line_i + 1
    pass  # print(f"checking top {t_top_i=} on line {_h_line_i=}")
    if t_top_i in range(len(_map)):
        if _map[_h_line_i][t_top_i] == TAIL:
            pass  # print(f"{TAIL} is on the top of {HEAD}")
            return True
    else:
        pass  # print(f"{t_top_i} not in {range(len(_map))}")

    t_bottom_i = h_i
    _h_line_i = h_line_i - 1
    pass  # print(f"checking bottom {t_bottom_i=} on line {_h_line_i=}")
    if t_bottom_i in range(len(_map)):
        if _map[_h_line_i][t_bottom_i] == TAIL:
            pass  # print(f"{TAIL} is on the bottom of {HEAD}")
            return True
    else:
        pass  # print(f"{t_bottom_i} not in {range(len(_map))}")

    t_diag_top_left_i = h_i - 1
    _h_line_i = h_line_i - 1
    # print(f"checking top-left(diagonally) {t_diag_top_left_i=} on line {_h_line_i=}")
    pass
    if t_diag_top_left_i in range(len(_map)) and t_diag_top_left_i in range(len(_map[0])):
        if _map[_h_line_i][t_diag_top_left_i] == TAIL:
            pass  # print(f"{TAIL} is on the top-left(diagonally) of {HEAD}")
            return True
    else:
        # print(f"either {t_diag_top_left_i} not in {range(len(_map))} OR {t_diag_top_left_i} in {range(len(_map[0]))}")
        pass

    t_diag_top_right_i = h_i + 1
    _h_line_i = h_line_i - 1
    # print(f"checking top-right(diagonally) {t_diag_top_right_i=} on line {_h_line_i=}")
    pass
    if t_diag_top_right_i in range(len(_map)) and t_diag_top_right_i in range(len(_map[0])):
        if _map[_h_line_i][t_diag_top_right_i] == TAIL:
            pass  # print(f"{TAIL} is on the top-right(diagonally) of {HEAD}")
            return True
    else:
        # print(f"either {t_diag_top_right_i} not in {range(len(_map))} OR {t_diag_top_right_i} not in {range(len(_map[0]))}")
        pass

    t_diag_bottom_left_i = h_i - 1
    _h_line_i = h_line_i + 1
    # print(f"checking bottom-left(diagonally) {t_diag_bottom_left_i=} on line {_h_line_i=}")
    pass
    if t_diag_bottom_left_i in range(len(_map)) and t_diag_bottom_left_i in range(len(_map[0])):
        if _map[_h_line_i][t_diag_bottom_left_i] == TAIL:
            # print(f"{TAIL} is on the bottom-left(diagonally) of {HEAD}")
            pass
            return True
    else:
        # print(f"either {t_diag_bottom_left_i} not in {range(len(_map))} OR {t_diag_bottom_left_i} in {range(len(_map[0]))}")
        pass

    t_diag_bottom_right_i = h_i + 1
    _h_line_i = h_line_i + 1
    # print(f"checking bottom-right(diagonally) {t_diag_bottom_right_i=} on line {_h_line_i=}")
    pass
    if t_diag_bottom_right_i in range(len(_map)) and t_diag_bottom_right_i in range(len(_map[0])):
        if _map[_h_line_i][t_diag_bottom_right_i] == TAIL:
            # print(f"{TAIL} is on the bottom-right(diagonally) of {HEAD}")
            pass
            return True
    else:
        # print(f"either {t_diag_bottom_right_i} not in {range(len(_map))} OR {t_diag_bottom_right_i} in {range(len(_map[0]))}")
        pass

    return False


if __name__ == '__main__':
    maps = generate_maps()
    for idx, _map in enumerate(maps):
        is_correct = verify_final_map(_map)
        print(f'{idx} is {is_correct}')
