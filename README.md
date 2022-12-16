# https://adventofcode.com/2022

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python ./day01/part1.py ./day01/input.txt
71124
> 764 μs
+ python ./day01/part2.py ./day01/input.txt
204639
> 689 μs
+ python ./day02/part1.py ./day02/input.txt
11841
> 1427 μs
+ python ./day02/part2.py ./day02/input.txt
13022
> 1425 μs
+ python ./day03/part1.py ./day03/input.txt
7553
> 766 μs
+ python ./day03/part2.py ./day03/input.txt
2758
> 464 μs
+ python ./day04/part1.py ./day04/input.txt
448
> 1811 μs
+ python ./day04/part2.py ./day04/input.txt
794
> 1941 μs
+ python ./day05/part1.py ./day05/input.txt
FJSRQCFTN
> 2096 μs
+ python ./day05/part2.py ./day05/input.txt
CJVLJQPHS
> 1276 μs
+ python ./day06/part1.py ./day06/input.txt
1848
> 764 μs
+ python ./day06/part2.py ./day06/input.txt
2308
> 1645 μs
+ python ./day07/part1.py ./day07/input.txt
1315285
> 938 μs
+ python ./day07/part2.py ./day07/input.txt
9847279
> 926 μs
+ python ./day08/part1.py ./day08/input.txt
1711
> 470 ms
+ python ./day08/part2.py ./day08/input.txt
301392
> 472 ms
+ python ./day09/part1.py ./day09/input.txt
6494
> 9533 μs
+ python ./day09/part2.py ./day09/input.txt
2691
> 36673 μs
+ python ./day10/part1.py ./day10/input.txt
11720
> 343 μs
+ python ./day10/part2.py ./day10/input.txt
####.###...##..###..####.###...##....##.
#....#..#.#..#.#..#.#....#..#.#..#....#.
###..#..#.#....#..#.###..#..#.#.......#.
#....###..#....###..#....###..#.......#.
#....#.#..#..#.#.#..#....#....#..#.#..#.
####.#..#..##..#..#.####.#.....##...##..

> 311 μs
+ python ./day11/part1.py ./day11/input.txt
95472
> 39425 μs
+ python ./day11/part2.py ./day11/input.txt
17926061332
> 11745 ms
+ python ./day12/part1.py ./day12/input.txt
408
> 28047 μs
+ python ./day12/part2.py ./day12/input.txt
399
> 1911 ms
+ python ./day13/part1.py ./day13/input.txt
5720
> 1865 μs
+ python ./day13/part2.py ./day13/input.txt
23504
> 117 ms
+ python ./day15/part1.py ./day15/input.txt
4879972
> 4307 ms
+ python ./day15/part2.py ./day15/input.txt
12525726647448
> 120 ms
```

```console
+ pytest -qq ./day01/part1.py ./day01/part2.py
..                                                                             [100%]
+ pytest -qq ./day02/part1.py ./day02/part2.py
..                                                                             [100%]
+ pytest -qq ./day03/part1.py ./day03/part2.py
..                                                                             [100%]
+ pytest -qq ./day04/part1.py ./day04/part2.py
..                                                                             [100%]
+ pytest -qq ./day05/part1.py ./day05/part2.py
..                                                                             [100%]
+ pytest -qq ./day06/part1.py ./day06/part2.py
.........                                                                      [100%]
+ pytest -qq ./day07/part1.py ./day07/part2.py
..                                                                             [100%]
+ pytest -qq ./day08/part1.py ./day08/part2.py
..                                                                             [100%]
+ pytest -qq ./day09/part1.py ./day09/part2.py
...                                                                            [100%]
+ pytest -qq ./day10/part1.py ./day10/part2.py
..                                                                             [100%]
+ pytest -qq ./day11/part1.py ./day11/part2.py
..                                                                             [100%]
+ pytest -qq ./day12/part1.py ./day12/part2.py
..                                                                             [100%]
pytest -qq ./day13/part1.py ./day13/part2.py
..                                                                             [100%]
pytest -qq ./day15/part1.py ./day15/part2.py
..                                                                             [100%]
```

```console
$ ./scripts/execute.sh
```
