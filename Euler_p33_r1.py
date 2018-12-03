# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 33 from project euler.org

Worked on 
2018/09/30 ()

@author: Jon
"""

num = 1
den = 1

# find fractions that satisfy conditions, store products of numerators and 
# denominators in num and den, respectively

for i in range(11,51):
    
    for j in range(11,100):
        
        if '0' in str(i) or '0' in str(j):
            # do nothing if i or j contain 0s
            continue
        
        elif i/j == 1:
            # do nothing if i and j are the same numbers
            continue
        
        elif int(str(i)[0]) == int(str(str(j)[1])) \
            and int(str(i)[1])/int(str(j)[0]) == i/j:
            num *= i
            den *= j
            
        elif int(str(i)[1]) == int(str(str(j)[0])) \
            and int(str(i)[0])/int(str(j)[1]) == i/j:
            num *= i
            den *= j


# convert fraction to lowest common terms
for i in range(num,0,-1):
    
    if num%i == 0 and den%i == 0:
        num /= i
        den /= i
        print(i)

print(num, den)