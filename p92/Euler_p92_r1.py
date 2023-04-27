# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:43:57 2018

Problem 92 from project euler.org

Worked on 
2018/09/25 (solved, takes a few minutes to run)

@author: Jon
"""


def square(n):
    # computes the sum of the square for each digit,i, in a number,n
    total = 0
    for i in range(0,len(str(n))):
        total += int(str(n)[i])**2
    return total

count = 0
for i in range(1,10000000):
    # cycle though numbers between 1 and ten million
    
    total = i
    while total != 1 and total != 89:
        total = square(total)
        
    if total == 89:
        count += 1

print(count)
