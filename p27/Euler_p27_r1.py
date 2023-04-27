# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:23:25 2018

Problem 27 from project euler.org

Worked on 
2018/09/30 (solved)

@author: Jon
"""

def is_prime(n):
    # checks if n is prime
    # returns True if n is prime, False if n is not prime
    
    # make sure n is positive
    if n < 0:
        n *= -1
    
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(n-1,1,-1):
            if n%i == 0:
                return False
        return True
    
def func(a,b,n):
    # calculates quadratics according to the problem
    result = n**2+a*n+b
    return result


max = 0 # keep track of maximum number of consecutive primes

for a in range(-999,1000):
    print(a)
    for b in range(-1000,1001):
        
        n = 0
        while is_prime(func(a,b,n)) == True:
            
            if n > max:
                max = n
                max_a = a
                max_b = b
            n += 1


print(max,max_a,max_b,max_a*max_b)