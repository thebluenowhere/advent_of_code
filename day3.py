#!/usr/bin/env python3

file = open('input3.txt', 'r')
i = [data.strip() for data in file.readlines()]

gamma = []
epsilon = []

def gamma(i):
    zeroCount = 0
    oneCount = 1
    for x in lines:
        if x[i] == '0':
            zeroCount += 1
        else:
            oneCount += 1
        if zeroCount > oneCount:
            return '0'
        else:
            return '1'



    dig0 = data[0]
    list.append(data[0])

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
