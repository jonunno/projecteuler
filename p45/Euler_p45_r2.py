# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:19:56 2018

Problem 45 from project euler.org

Worked on 
2018/09/24 (solved, much faster than r1)

@author: Jon
"""

def tri(n):
    # calculate and return triangle number 
    num = n*(n+1)/2
    return num

def pent(n):
    # calculate and return pentagonal number
    num = n*(3*n-1)/2
    return num

def hexa(n):
    # calculate and return hexagonal number
    num = n*(2*n-1)
    return num

i = 300 # counter for trinagle numbers
triangle = tri(i)
j = 300 # counter for pentagonal numbers
pentagonal = pent(j)
k = 300 # counter for hexagonal numbers
hexagonal = hexa(k)

while triangle != pentagonal or triangle != hexagonal:
    
    # check which number is the smallest and increment the corresponing counter
    if triangle < pentagonal and triangle < hexagonal:
        i += 1
        triangle = tri(i)
    elif pentagonal < triangle and pentagonal < hexagonal:
        j += 1
        pentagonal = pent(j)
    elif hexagonal < triangle and hexagonal < pentagonal:
        k += 1
        hexagonal = hexa(k)
    else:
        i += 1
        triangle = tri(i)

print(triangle, pentagonal, hexagonal)