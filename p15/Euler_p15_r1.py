# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:17:37 2018

Problem 15 from project euler.org

Worked on 
2018/09/23 
2018/09/24

@author: Jon
"""

# set the dimensions of the grid
dim = 3

num_path = 0


for i in range(0,dim+1):
    
    num_path += i+1
    
print(num_path)

"""
for i in range(0,dim+1):
    
    for j in range(0,dim):
        
        num_path += 1
        
print(num_path)
"""