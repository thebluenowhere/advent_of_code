#!/usr/bin/env python3

file = open('input3.txt', 'r')
i = [data.strip() for data in file.readlines()]

gamma = []
epsilon = []
list = []

for data in i:
    dig0 = data[0]
    dig1 = data[1]
    dig2 = data[2]
    dig3 = data[3]
    dig4 = data[4]
    dig5 = data[5]
    dig6 = data[6]
    dig7 = data[7]
    dig8 = data[8]
    dig9 = data[9]
    list.append(data[0])
    list.append(data[1])
    list.append(data[2])
    list.append(data[3])
    list.append(data[4])
    list.append(data[5])
    list.append(data[6])
    list.append(data[7])
    list.append(data[8])
    list.append(data[9])

index0a = list.count('0')
index0b = list.count('1')

if index0a > index0b:
    gamma.append(0)
    epsilon.append(1)
else:
    gamma.append(1)
    epsilon.append(0)


print('The gamma rate is: ' + str(gamma))
print('The epsilon rate is: ' + str(epsilon))
