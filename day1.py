#!/usr/bin/env python3
# Part 1:

file = open('input.txt', 'r')

depths = [int(data) for data in file.readlines()]
count = 0

for data in range(0, len(depths) -1):
    d1 = depths[data]
    d2 = depths[data+1]

    if d1 < d2:
        count = count + 1
print(count)

# Part 2:

file = open('input.txt', 'r')

depths = [int(data) for data in file.readlines()]
count = 0

for data in range(0, len(depths) -3):
    d1 = depths[data]
    d2 = depths[data+3]

    if d1 < d2:
        count = count + 1
print(count)
