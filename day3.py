#!/usr/bin/env python3

file = open('input3.txt', 'r')
fileLines = [data.strip() for data in file.readlines()]


def binary():

    for lines in fileLines:
        for i in lines:
            print(lines)
            print(i)
            for i in range(12):
                print(i)
                zeroCount = str(i.count("0"))
                onesCount = str(i.count("1"))
                if zeroCount > onesCount:
                    gamma = "0"
                    epsilon = "1"
                else:
                    gamma = "1"
                    epsilon = "0"
                    return gamma
                return epsilon
print(binary())
