#!/usr/bin/env python3

file = open('input3.txt', 'r')
i = [data.strip() for data in file.readlines()]

binary = []
list = []
for data in i:
    dig1 = data[0]
    list.append(data[0])

for n in list:
    count_0 = list.count('0')
    count_1 = list.count('1')
    if count_1 > count_0:
        binary.append('1')
    else:
        binary.append('0')
print(binary)
