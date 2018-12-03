# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:04:20 2018

Problem 12 from project euler.org

Worked on 
2018/09/22 (solution probably works but takes too long)
2018/09/22 

@author: Jon
"""

def triangle(n):
    # computes the nth triangle number
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# create array of triangle numbers
triangle_list = []
n = 7
for i in range(1,n):
    triangle_list.append(tri(i))
    
    
# the triangle number will have divisors that must reduce to prime numbers,
# therefore, try all combinations of prime numbers that result in 500 divisors, 
# using larger primes if necessary
    
# Find n prime numbers
def prime(n):
    # returns an array of the first n prime numbers
    primes = []
    i = 1 # counter to keep track of number to test if prime
    while len(primes) < n:
        
        i += 1
        
        for j in range(2,i+1):
            if i == j:
            # i was not divisible by any number in the for loop, it is prime
                primes.append(i)
                
            elif i%j == 0:
                # i is divisible by j and therefore not prime
                break
    return primes

prime_list = prime(10)

# Test all combinations of primes to form a triangle number with at least d divisors
div = 5 # note, since 1 and the triangle number are divisors, there will be a max
      # of d-2 prime divisors

# initialize a list, prod, to store combinations of prime multiples
prod = []
num = 0 
for i in range(0,div-2):
    
    