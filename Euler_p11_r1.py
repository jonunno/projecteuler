# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:00:33 2018
Problem 11 from project euler.org

Worked on 
2018/09/22 (solved, answer 70600674)

@author: Jon


"""

import numpy

# initialize grid
grid = []

# import grid of numbers
with open('Euler_p11_num.txt') as textfile:
    grid = textfile.read()

# split the string stored in grid to make a list
grid = grid.split()

# reshape the list to a 20 x 20 grid
dim = 20
grid = numpy.reshape(grid,(dim,dim))

# solve problem
num = 4 # product of 4 numbers

# initialize prod, a matrix to store products
prod = numpy.ones((dim,dim))

# check products in each row
# X X X
# X X X
# 0 0 0

for i in range(0,dim): # cycle through row
    
    for j in range(0,dim-num+1): # cycle through components of a row, by looking at each column
        
        prod[i,j] = 1
        
        for k in range(0,num):
            
            prod[i,j] *= int(grid[i,j+k])

max_horizontal = numpy.max(prod)

# reset prod matrix
prod = numpy.ones((dim,dim))

# check products in each column
# 0 X X
# 0 X X
# 0 X X
for i in range(0,dim-num+1): # cycle through column
    
    for j in range(0,dim): # cycle through components of a column
        
        prod[i,j] = 1
        
        for k in range(0,num):
            
            prod[i,j] *= int(grid[i+k,j])
    
max_vertical = numpy.max(prod)

# check diagonals

# check diagonal from top left to bottom right
# 0 X X
# X 0 X
# X X 0

# reset prod matrix
prod = numpy.ones((dim,dim))

for i in range(num-1,dim):
    
    for j in range(num-1,dim):
        
        for k in range(0,num):
            
            prod[i,j] *= int(grid[i-k,j-k])
            
max_left_diag = numpy.max(prod)

# check diagonal from top right to bottom left
# X X 0
# X 0 X
# 0 X X

# reset prod matrix
prod = numpy.ones((dim,dim))

for i in range(0,dim-num+1):
    
    for j in range(num-1,dim):
        
        for k in range(0,num):
            
            prod[i,j] *= int(grid[i+k,j-k])
            
max_right_diag = numpy.max(prod)

# gather maximum values
maxes = [max_vertical,
         max_horizontal,
         max_left_diag,
         max_right_diag]

answer = max(maxes)
print(answer)



