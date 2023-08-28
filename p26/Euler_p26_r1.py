# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 26 from project euler.org

Worked on 
2018/09/28 ()
2023/08/27

@author: Jon
"""
import numpy as np


domain = range(1, 1000 + 1)

for d in domain:
    fraction = np.longdouble(1/d)
    print([d, fraction])

