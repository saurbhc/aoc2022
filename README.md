# Advent of Code 2022

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python ./day01/part1.py ./day01/input.txt
71124
> 636 μs
+ python ./day01/part2.py ./day01/input.txt
204639
> 696 μs
+ python ./day02/part1.py ./day02/input.txt
11841
> 1513 μs
+ python ./day02/part2.py ./day02/input.txt
13022
> 1428 μs
+ python ./day03/part1.py ./day03/input.txt
7553
> 772 μs
+ python ./day03/part2.py ./day03/input.txt
2758
> 450 μs
+ python ./day04/part1.py ./day04/input.txt
448
> 1800 μs
+ python ./day04/part2.py ./day04/input.txt
794
> 1500 μs
```

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'pytest -qq {}/part*.py;'
+ pytest -qq ./day01/part1.py ./day01/part2.py
..                                                                                                                                                                                        [100%]
+ pytest -qq ./day02/part1.py ./day02/part2.py
..                                                                                                                                                                                        [100%]
+ pytest -qq ./day03/part1.py ./day03/part2.py
..                                                                                                                                                                                        [100%]
+ pytest -qq ./day04/part1.py ./day04/part2.py
..                                                                                                                                                                                        [100%]
```

```console
$ ./scripts/execute.sh
```
