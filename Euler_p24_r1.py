# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:09:29 2018

Problem 24 from project euler.org

Worked on 
2018/10/01 ()

@author: Jon
"""

import numpy

lim = 3


for i in range(0,lim):
    for j in range(0,lim):
        if i == j:
            continue
        for k in range(0,lim):
            if i == k or j == k:
                continue
            print(i,j,k)
# code works for test example but it's not well structured
print('---')
lim = 3

num = list(range(0,lim))
used = [None]*lim


for i in range(0,lim):
    used = [None]*lim
    used[num[i]] = num[i]
    for j in range(0,len(num)):
        
        if j in used:
            continue
        used[num[j]] = num[j]
        
        for k in range(0,len(num)):
            if k in used:
                continue
            print(i,j,k)