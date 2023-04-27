# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:06:02 2018

Problem 25 from project euler.org

Worked on 
2018/09/25 (move to r2, this is an inefficient way to solve the problem)

@author: Jon
"""

import numpy

def fib(n):
# returns an array with fibonacci numbers up to n
    
    # create array of length n
    res = numpy.zeros(n,dtype=int)
    
    res[0] = 1
    res[1] = 1
    
    for i in range(2,len(res)):
        res[i] = res[i-1] + res[i-2]
    return res

n = 300000
fibonacci = fib(n)

while len(str(fibonacci[len(fibonacci)-1])) < 1000:
    n += 1
    fibonacci = fib(n)
    print(n)
    

