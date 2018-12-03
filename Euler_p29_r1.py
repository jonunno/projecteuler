# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 29 from project euler.org

Worked on 
2018/09/28 
2018/09/30 (solved, after fiddling around with the break statements)

@author: Jon
"""

count = 0 # keep track of the number of distinct terms in sequence

lim = 100

for a in range(2,lim+1):
    
    for b in range(2,lim+1):
        
        num = a**b
        
        breaker = 0
        repeat = 0
        
        for dum_a in range(2,a):
            for dum_b in range(b,lim+1):
                
                if dum_a**dum_b == num:
                    repeat = 1
                    breaker = 1
                    break
                elif dum_a**dum_b > num:
                    break
                
            if breaker == 1:
                break
        
        if repeat == 0:
            count += 1
            
print(count)    

    
    
    