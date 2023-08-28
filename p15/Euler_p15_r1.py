# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:17:37 2018

Problem 15 from project euler.org

Worked on 
2018/09/23 
2018/09/24
2023/08/26

@author: Jon
"""

dimension = 2
n_right = dimension
n_down = dimension

routes = []

# def add_step(step_list, step_type, step_type_remaining):
#     result = step_list
#     if step_type_remaining > 0:
#         result.append(step_type)
#         step_type_remaining -= 1
#     return result, step_type_remaining

# print(add_step([], "d", 3))    
 
# print(add_step([], "r", 3))    


# lists = [[""]]
# def gen(lists, rights, downs):
#     add_right_step = lists.copy()
#     add_down_step = lists.copy()
#     for list in lists:
#         if (rights > 0):
#             rights -= 1
#             add_right_step.append(list + ["r"])
#             # print(add_right_step)
#             add_right_step = gen(add_right_step, rights, downs)
#         if (downs > 0):
#             downs -= 1
#             add_down_step.append(list + ["d"])
#             # print(add_down_step)
#             add_down_step = gen(add_down_step, rights, downs)
    
#     return add_right_step + add_down_step #+ add_down_step
# lists = gen(lists, 1, 1)
# print(lists)


# def gen(list, rights, downs):
#     right_step = list.copy()
#     down_step = list.copy()
#     if rights > 0:
#         right_step = right_step + ["r"]
#         right_step = gen(right_step, rights-1, downs)
#     if downs > 0:
#         down_step = down_step + ["d"]
#         down_step = gen(down_step, rights, downs-1)
#     if(rights == 0 & downs == 0):
#         return [right_step , down_step]

#     return [gen(right_step, rights, downs) , gen(down_step, rights, downs)]

# print(gen([], 4, 4))


# def gen(list, i, j):
#     # print(i)
#     # print(list)    
#     right = list.copy()
#     down = list.copy()
#     if i > 0:
#         return gen(right + ["a"], i-1, j), gen(down + ["d"], i-1, j)
#     if j > 0:
#         return gen(right + ["a"], i, j-1), gen(down + ["d"], i, j-1)
#     if i + j == 0:
#         return right, down


#     return gen(right, i-1), gen(down, i-1)
# print(gen([], 2, 1))


# def gen(list, i, j):
#     copy = list.copy()
#     # print(i, j, copy)
#     if i > 0 and j > 0 :
#         return gen(copy + ["r"], i-1, j), gen(copy + ["d"], i, j-1)
#     elif i > 0:
#         return gen(copy + ["r"], i-1, j) 
#     elif j > 0:
#         return gen(copy + ["d"], i, j-1)
#     else :
#         print(copy)
#         return copy

# routes_raw = gen([], 6, 6)

# IT WORKS!!! it generates all combinations of 2 characters with the the number of characters constrained

# but the output is a bit wonky - lots of nested tuples and lists

# routes = []

# def flatten_tuple(nested_tuples):
#     if isinstance(nested_tuples, tuple):
#         for item in nested_tuples:
#             yield from flatten_tuple(item)
#     else:
#         yield nested_tuples
# routes = list(flatten_tuple(routes_raw))
# print(list(routes))
# print(len(routes))
# now solve the actual problem...

# takes ages to run, look at applying a bit of math

# 1x1: 2 routes
# 2x2: 6 routes
# 3x3: 20 routes
# 4x4: 70
# 5x5: 252
# 6x6: 924

# 1: 2
# 2: 6:     2+2+1+1
# 3: 20:    6+6+3+3+1+1 (6=routes from prior square, 3=2+1)
# 4: 70:    20+20+10+10+4+4+1+1 (20=routes from prior square, 10=6+3+1, 4=3+1)
# 5: 252    70+70+35+35+15+15+5+5+1+1 (70=routes from prior square. 35=20+10+4+1, 15=10+4+1, 5=4+1)
# ...

routes = [2, 1]
dimension = 0
for dimension in range(3, 20+1):
    old_routes = routes.copy()
    routes = []
    routes.append(2*sum(old_routes))
    for i in range(0, len(old_routes)-1):
        routes.append(sum(old_routes[i:]))
    routes.append(1)
    print(routes)
    print(sum(routes)*2)

# solved 137846528820 