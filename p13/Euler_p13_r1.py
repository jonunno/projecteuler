# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 11:56:37 2018

Problem 13 from project euler.org

Worked on 
2018/09/23 (solved)

@author: Jon
"""

# open and read textfile containing the 50 numbers
with open('Euler_p13_num.txt') as textfile:
    grid = textfile.read()
    
# organize the numbers into individual list elements
grid = grid.split()

# initialize variable to store sum
sum = 0

for i in range(0,len(grid)):
    sum += int(grid[i])

print(str(sum)[0:10])