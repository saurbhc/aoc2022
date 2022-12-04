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
> 945 μs
+ python ./day01/part2.py ./day01/input.txt
204639
> 741 μs
+ python ./day02/part1.py ./day02/input.txt
11841
> 1936 μs
+ python ./day02/part2.py ./day02/input.txt
13022
> 1450 μs
+ python ./day03/part1.py ./day03/input.txt
7553
> 762 μs
+ python ./day03/part2.py ./day03/input.txt
2758
> 692 μs
+ python ./day04/part1.py ./day04/input.txt
448
> 1820 μs
+ python ./day04/part2.py ./day04/input.txt
794
> 1499 μs
```
