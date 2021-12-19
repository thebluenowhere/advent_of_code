#!/usr/bin/env python3

file = open('input3.txt', 'r')
fileLines = [data.strip() for data in file.readlines()]

gamma = ""
epsilon = ""

for i in range(12):
    oneCount = 0
    zeroCount = 0
    for line in fileLines:
        if line[i] == "1":
            oneCount += 1
        else:
            zeroCount += 1

    if oneCount > zeroCount:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)
