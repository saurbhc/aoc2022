#!/usr/bin/env bash

find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'pytest -qq {}/part*.py;'
