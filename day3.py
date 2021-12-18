#!/usr/bin/env python3

file = open('input3.txt', 'r')
lines = [data.strip() for data in file.readlines()]
print(lines)
gamma = ""
epsilon = ""
digits = ""

for i in lines[i]:

    digits = digits + str(lines[i])
    #print(digits)
    zero = digits.count('0')
    ones = digits.count('1')
    if zero > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    digits = ""
