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
> 697 μs
+ python ./day01/part2.py ./day01/input.txt
204639
> 2223 μs
+ python ./day02/part1.py ./day02/input.txt
11841
> 3220 μs
+ python ./day02/part2.py ./day02/input.txt
13022
> 1739 μs
+ python ./day03/part1.py ./day03/input.txt
7553
> 871 μs
+ python ./day03/part2.py ./day03/input.txt
2758
> 493 μs
+ python ./day04/part1.py ./day04/input.txt
448
> 1994 μs
+ python ./day04/part2.py ./day04/input.txt
794
> 1916 μs
+ python ./day05/part1.py ./day05/input.txt
FJSRQCFTN
> 1458 μs
+ python ./day05/part2.py ./day05/input.txt
CJVLJQPHS
> 1277 μs
+ python ./day06/part1.py ./day06/input.txt
1848
> 1108 μs
+ python ./day06/part2.py ./day06/input.txt
2308
> 1420 μs
+ python ./day07/part1.py ./day07/input.txt
1315285
> 988 μs
+ python ./day07/part2.py ./day07/input.txt
9847279
> 944 μs
+ python ./day08/part1.py ./day08/input.txt
1711
> 353 ms
+ python ./day08/part2.py ./day08/input.txt
301392
```

```console
+ pytest -qq ./day01/part1.py ./day01/part2.py
..                                                                                                           [100%]
+ pytest -qq ./day02/part1.py ./day02/part2.py
..                                                                                                           [100%]
+ pytest -qq ./day03/part1.py ./day03/part2.py
..                                                                                                           [100%]
+ pytest -qq ./day04/part1.py ./day04/part2.py
..                                                                                                           [100%]
+ pytest -qq ./day05/part1.py ./day05/part2.py
..                                                                                                           [100%]
+ pytest -qq ./day06/part1.py ./day06/part2.py
.........                                                                                                    [100%]
+ pytest -qq ./day07/part1.py ./day07/part2.py
..                                                                                                           [100%]
+ pytest -qq ./day08/part1.py ./day08/part2.py
..
```

```console
$ ./scripts/execute.sh
```
