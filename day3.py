#!/usr/bin/env python3

file = open('input3.txt', 'r')
fileOpen = [data.strip() for data in file.readlines()]
gamma = ""
epsilon = ""
digits = ""

for lines in fileOpen:
    i = lines[0]
    for lines[i] in range(12):
        digits = digist + lines[i]
        print(digits)
        zero = digits.count('0')
        ones = digits.count('1')
        if zero > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamme += '1'
            epsilon += '0'
            digits = ""
