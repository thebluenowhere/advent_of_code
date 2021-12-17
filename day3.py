#!/usr/bin/env python3

file = open('input3.txt', 'r')
i = [data.strip() for data in file.readlines()]

binary = []
list = []
for data in i:
    dig1 = data[0]
    list.append(data[0])

index1a = list.count(0)
index1b = list.count(1)

if index1a > index1b:
    binary.append(index1a)
else:
    binary.append(index1b)

print(binary)

