# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:06:02 2018

Problem 25 from project euler.org

Worked on 
2018/09/25 (move to r2, this is an inefficient way to solve the problem)
2018/09/25 (solved in r2)

@author: Jon
"""




fn1 = 1
fn2 = 1
fn = fn1 + fn2
n = 2

while len(str(fn)) < 1000:
    fn1 = fn2
    fn2 = fn
    fn = fn1 + fn2
    n += 1
    print(n)
    
# answer is n+1 since n is an index that starts at 0

