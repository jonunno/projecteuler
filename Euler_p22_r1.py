# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 22:29:32 2018

Problem 22 from project euler.org

Worked on 
2018/09/24 (solved)

@author: Jon
"""
# read textfile
with open('Euler_p22_names.txt') as textfile:
    names = textfile.read()

# remove quotse and split long string by comma
names = names.replace('"','')
names = names.split(',')

dum = []

for i in range(0,int(len(names)*2)): # the range of i is hard coded (not ideal)
    # i is the counter associated with the number of times 
    for j in range(0+i%2,len(names)-1):
        # sort names by alphabetical order, compare pairs of names and swap if
        # out of order
        if names[j]>names[j+1]:
            dum = names[j]
            names[j] = names[j+1]
            names[j+1] = dum

sum = 0
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',\
        'R','S','T','U','V','W','X','Y','Z']

for i in range(0,len(names)):
    # calculate the value for each name and add it to sum
    
    name_sum = 0
    for j in range(0,len(names[i])):
        
        for k in range(0,len(alph)):
            
            if names[i][j] == alph[k]:
                name_sum += k+1
    
    sum += name_sum*(i+1)
    
    
print(sum)