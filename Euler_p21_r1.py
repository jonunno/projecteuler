# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:53:08 2018

Problem 21 from project euler.org

Worked on 
2018/10/01 (solved)

@author: Jon
"""
def sum_divisor(n):
    # finds and sums the divisors of n
    # returns the sum of divisors
    
    sum_div = 0
    
    for i in range(1,n):
        # test all numbers from 1 to (not including) n and test if they are divisors
        
        if n%i == 0:
            # i is a divisor of n, add to sum_div
            sum_div += i
    
    return sum_div

# test the function sum_divisor()
print(sum_divisor(284))
print(sum_divisor(220))

count = 0 # count the number of amicable numbers
sum_amic = 0 # record the sum of amicable numbers

for i in range(2,10000):
    # test all numbers from 2 to (not including) 10000
    
    if i == sum_divisor(sum_divisor(i)) and i != sum_divisor(i):
        # i is an amicable number
        # note: in the future, I can add an optimization to reduce testing
        #   amicable numbers twice
        count += 1
        sum_amic += i

print(count, sum_amic)