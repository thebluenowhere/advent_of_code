#!/usr/bin/env python3

file = open('input3.txt', 'r')
lines = [data.strip() for data in file.readlines()]

gamma = ""
epsilon = ""
digits = ""

for i in range(12):
    for x in lines[i]:
        digits = digits + str(lines[i])
        zero = digits.count('0')
        ones = digits.count('1')
        if zero > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
        digits = ""

print(gamma)
print(epsilon)
