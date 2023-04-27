# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:23:16 2018

Problem 49 from project euler.org

Worked on 
2018/09/24 (solved)

@author: Jon
"""
import numpy

def isprime(n):
    # determine if a number is prime
    
    if n == 2:
        return True
    
    for i in range(2,n):
        
        if n%i == 0: # number is not prime 
            return False
        
        elif i == n-1:
            return True
        
        
def isperm(num1,num2):
    # determine if num1 and num2 both contain the same numbers
    # num1 and num2 should both be the same length
    
    check = numpy.zeros(len(str(num1)), dtype=bool)
    for i in range(0,len(str(num1))):
        check[i] = False
    
    
    
    for i in range(0,len(str(num1))):
        
        for j in range(0,len(str(num2))):
            
            if str(num1)[i] == str(num2)[j]:
                check[i] = True
                
    # deal with repeated numbers by making sure num1 contains all numbers in num2
    for i in range(0,len(str(num2))):
        
        for j in range(0,len(str(num1))):
            
            if str(num2)[i] == str(num1)[j]:
                break
            elif j == len(str(num1))-1:
                check[i] = False
    
    
    
    for i in range(0,len(check)):
        if check[i] == False:
            return False
        elif i == len(check)-1:
            return True
    
    
"""
Notes: since I'm looking for three 4 digit primes, the increment must be less 
than 10,000/3 (3333 or less)

"""



for i in range(3333,0,-1):
    # loop through the increment sizes
    
    for j in range(1000,10000-2*3333):
        # first check if j is prime
        
        if isprime(j) == True:
            # j is prime, check if j+i and j+2*i are both prime
            
            if isprime(j+2*i) == True and isprime(j+2*i) == True:
                # j is prime and the start of a sequence of primes
            
                # check if the numbers in the series are permutations of one another
                if isperm(j,j+i) == True and isperm(j,j+2*i) == True:
                    print(j, j+i, j+2*i)
                    




