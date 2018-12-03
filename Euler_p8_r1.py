# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:14:48 2018
Problem 8 from project euler.org

Worked on 
2018/09/22 (solved, answer 23514624000)


@author: Junno
"""
import numpy


# initialize num variable
num = []

# import numbers and store in num
with open('Euler_p8_num.txt') as textfile:
    for line in textfile.readlines():
        num+=(line)
        
# remove newline characters ('\n')
while '\n' in num:
    num.remove('\n')

# solve problem
k = 0
prod = numpy.zeros((len(num),1))
for i in range(0,len(num)-13):
    res = 1
    for j in range(0,13):
        res *= int(num[k+j])
    prod[k] = res
    k += 1


# find max value in prod
max = numpy.max(prod)

print(max)