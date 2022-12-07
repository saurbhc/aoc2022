from __future__ import annotations

import argparse
import operator
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


# This will act as a Double Linked List
class Dir:
    def __init__(self, data):
        self.data = data
        self.next, self.prev = [], None
        self.children = []
        self.size = 0

    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        return f'{self.data} ({self.size}) prev={self.prev.data if self.prev else None} next={[i.data for i in self.next]}'

    def __repr__(self):
        return f'{self.data} ({self.size}) prev={self.prev.data if self.prev else None} next={[i.data for i in self.next]}'


def compute(s: str) -> int:
    all_dirs = []
    dir_sizes = {}
    root_dir, current_dir = None, None

    for block in s[2:].split('\n$'):
        block = block.strip()
        block_lines = block.splitlines()
        command, output = block_lines[0], block_lines[1:]

        if command.startswith('cd'):
            _, _current_dir = command.split(' ')
            if _current_dir == '/':
                root_dir_obj = Dir(_current_dir)
                all_dirs.append(root_dir_obj)
                current_dir = root_dir_obj
                root_dir = current_dir
            elif _current_dir == '..':
                assert current_dir.prev
                nested_dir = current_dir

                current_dir = current_dir.prev
                # current_dir.size += nested_dir.size
            else:
                current_dir_obj = Dir(_current_dir)
                all_dirs.append(current_dir_obj)
                prev_node = current_dir
                prev_node.next.append(current_dir_obj)
                current_dir = current_dir_obj
                current_dir.prev = prev_node

        elif command.startswith('ls'):
            assert current_dir
            size = 0
            for output_line in output:
                first, file_name = output_line.split(' ')
                if first == 'dir':
                    continue
                else:
                    size += int(first)
            dir_sizes[current_dir] = size
            current_dir.size += size

    def get_dir_size(dir_obj):
        size = 0
        for nested_dir_obj in dir_obj.next:
            size += get_dir_size(nested_dir_obj)
        dir_obj.size += size
        return dir_obj.size

    get_dir_size(root_dir)
    sorted_dirs_by_size = sorted(all_dirs, key=operator.attrgetter('size'))
    at_most_size = 100000
    size = 0
    for dir_obj in all_dirs:
        if dir_obj.size <= at_most_size:
            # print(dir_obj)
            size += dir_obj.size

    return size


INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''
EXPECTED = 95437


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
