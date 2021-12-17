#!/usr/bin/env python3

file = open('input3.txt', 'r')
i = [data.strip() for data in file.readlines()]

gamma = []
epsilon = []
list = []

for data in i:
    dig1 = data[0]
    list.append(data[0])

index1a = list.count('0')
index1b = list.count('1')

if index1a > index1b:
    gamma.append(0)
    epsilon.append(1)

print('The gamma rate is: ' + str(gamma))
print('The epsilon rate is: ' + str(epsilon))
