# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 34 from project euler.org

Worked on 
2018/09/28 (solved)

@author: Jon
"""

# there is a maximum possible number that fits the description
# 9! = 362880, which is the maximum value that can be added to the sum by 
# including an extra digit

# 9! * 1 = 362880
# 9! * 2 = 725760
# 9! * 3 = 1088640
# 9! * 4 = 1451520
# 9! * 5 = 1814400
# 9! * 6 = 2177280, note 999999 is still less than 9! * 6
# 9! * 7 = 2540160, but 9999999 is greater than 9! * 7

# the tested number will be limited to 2540160


def fact(n):
    factorial = 1
 
    
    for i in range(n,0,-1):
        factorial *= i
        
    return factorial



int_sum = 0
total = 0

for i in range(3, 2540160):
    
    int_sum = 0
    
    for j in range(0,len(str(i))):
        
        int_sum += fact(int(str(i)[j]))
        
    if int_sum == i:
        total += int_sum
        
print(total)
    
    
    