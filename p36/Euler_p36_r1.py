# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 17:06:43 2018

Problem 36 from project euler.org

Worked on 
2018/09/28 ()

@author: Jon
"""


def calc_binary(n):
    # calculates the binary form of n
    result = []
    digits = 0
    power = 0
    remainder = n

    while n >= 2**digits:
        digits += 1

    for power in range(digits-1, 0, -1):
        result.append(int(remainder / 2**power))
        remainder -= 2**power * int(remainder / 2**power)
    result.append(remainder % 2)
    return result


def check_palindrome(n):
    for i in range(0, int(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True

pairs = []
binary = []
for i in range(1, 10**6):
    # print(i)
    if check_palindrome(list(str(i))):
        binary = calc_binary(i)
        if check_palindrome(binary):
            pairs.append(i)

print(pairs)
print(sum(pairs))
# correct answer 872187