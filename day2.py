#!/usr/bin/env python3
# PART 1
file = open('input2.txt', 'r')
i = [data.strip() for data in file.readlines()]


def solve(directions):
    horizontal = 0
    depth = 0
    for full_directions in directions:
        a, b = full_directions.split()
        b = int(b)

        if a == 'forward':
            horizontal += b
        if a == 'up':
            depth -= b
        if a == 'down':
            depth += b

    return horizontal * depth

print(solve(i))


#!/usr/bin/env python3
# PART 2
file = open('input2.txt', 'r')
i = [data.strip() for data in file.readlines()]


def solve(directions):
    horizontal = 0
    depth = 0
    aim = 0
    for full_directions in directions:
        a, b = full_directions.split()
        b = int(b)

        if a == 'forward':
            horizontal += b
            depth += aim * b
        if a == 'up':
            aim -= b
        if a == 'down':
            aim += b

    return horizontal * depth

print(solve(i))
