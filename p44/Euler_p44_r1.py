# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:32:27 2018
230827

@author: Junno

project euler problem 44
"""
def calc_pentagonal(n):
    return n*(3*n-1)/2

def check_pentagonal(pents, p):
    try:
        return pents.index(p)
    except:
        return -1


pentagonals = []


######
# first attempt, took a long time to run - slow at first, then got faster as the counter approached the length of the list
######

lim = 10000
for i in range(1, lim+1):
    pentagonals.append(calc_pentagonal(i))

# print(pentagonals)

# min_delta = pentagonals[lim-1]

# pentagonal_deltas = []

# for increment in range(1, 1000):
#     print(increment)
#     for i in range(1, lim-1-increment):
#         delta = pentagonals[i] - pentagonals[i+increment]
#         if delta < 0: delta *= - 1
#         if (check_pentagonal(pentagonals, delta) >= 0):
#             total = pentagonals[i] + pentagonals[i+increment]
#             if(check_pentagonal(pentagonals, total) >= 0):
#                 pentagonal_deltas.append([pentagonals[i], pentagonals[i+increment], delta])
#                 if delta < min_delta:
#                     min_delta = delta
#                 print(pentagonal_deltas[-1])

# print(min_delta)

######
# second attempt, took a long time to run, fast at first, then slowed down as counter progressed through the list
######

# min_delta = 0
# pentagonals.append(1)
# pentagonals.append(2)
# i = 3
# while True:
#     print("i: ", i, " min_delta: ", min_delta)
#     pentagonals.append(calc_pentagonal(i))
#     j = 0
#     while pentagonals[j] <= pentagonals[-1]/2+1:
#         # print("j: ", j)
#         delta = pentagonals[-1] - pentagonals[j]
#         if delta < 0: delta *= -1
#         if check_pentagonal(pentagonals, delta) >= 0:
#             total = pentagonals[-1] + pentagonals[j]
#             if (check_pentagonal(pentagonals, total) >= 0):
#                 print(pentagonals[-1], pentagonals[j], total, delta)
#                 min_delta = delta
#                 break
#         j += 1
#     # print(pentagonals[-1])
#     i += 1
#     if i > 1000000:
#         break
    

######
# third attempt, solve the formula directly
######

# tup = (2, 3)
# print(tup[0])
# sum_solutions = [(x, y) for x in range(0, 1000) for y in range(0, 1000) if (check_pentagonal(pentagonals, pentagonals[x] + pentagonals[y]) >= 0)]
# print(sum_solutions)

# delta_solutions = [(solution[0], solution[1]) for solution in sum_solutions if (check_pentagonal(pentagonals, pentagonals[solution[0]] - pentagonals[solution[1]]) >= 0)]
# print(delta_solutions)

lim = 100000
equation_solutions = [(x, y, z, a) for x in range(1, lim) for y in range(1, lim) for z in range(1, lim) for a in range(1, lim) if((x*(3*x-1) + y*(3*y-1) == z*(3*z-1)) & (x*(3*x-1) - y*(3*y-1) == a*(3*a-1)))]
print(equation_solutions)