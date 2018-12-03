# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:19:56 2018

Problem 45 from project euler.org

Worked on 
2018/09/24 (it works but takes a long time to run)

@author: Jon
"""
import numpy

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

# try the first n triangle numbers
    
n = 300000

triangle = numpy.zeros(n)
pentagonal = numpy.zeros(n)
hexagonal = numpy.zeros(n)

for i in range(0,n):
    # populate the triangle, pentagonal, and hexagonal arrays
    triangle[i] = tri(i)
    pentagonal[i] = pent(i)
    hexagonal[i]= hexa(i)
    
for i in range(0,len(hexagonal)):

    for j in range(0,len(pentagonal)):
        
        if hexagonal[i] == pentagonal[j]:
            
            for k in range(0,len(triangle)):
                
                if hexagonal[i] == triangle[k]:
                    
                    print(triangle[k],pentagonal[j],hexagonal[i])
                    print(k,j,i)
    
