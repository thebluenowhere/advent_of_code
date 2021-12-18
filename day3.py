#!/usr/bin/env python3

file = open('input3.txt', 'r')
lines = [data.strip() for data in file.readlines()]
print(lines)
gamma = ""
epsilon = ""
digits = ""
i = lines[0]

for lines in range(len(lines)):
    for lines[i] in range(12):
       digits = digits + lines[i]
       zero = digits.count('0')
       ones = digits.count('1')
       if zero > ones:
           gamma += '0'
           epsilon += '1'
       else:
           gamme += '1'
           epsilon += '0'
           digits = ""

