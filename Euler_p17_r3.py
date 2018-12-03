# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:21:29 2018

@author: Jon

ProjectEuler.net

Problem 17

---
Progress
    2018-11-24 (r1)
    2018-11-25 (r2)
    2018-12-02 (solved)
"""
import unittest

# Define functions

def add_zeros(num, total_len):
    """ add zeros to the start of an integer to make it a certain length and returns a string """
    result = str(num)
    while len(str(result)) < total_len:
        result = '0' + result
    return result

def build_number(num):
    """ builds a string for num, which is inputted as a string """

    # store text for each digit place
    thousands = {0:'',
                 1:'one thousand'}
    hundreds = {0:'',
                1:'one hundred',
                2:'two hundred',
                3:'three hundred',
                4:'four hundred',
                5:'five hundred',
                6:'six hundred',
                7:'seven hundred',
                8:'eight hundred',
                9:'nine hundred'}
    tens = {0:'',
            1:'ten',
            2:'twenty',
            3:'thirty',
            4:'forty',
            5:'fifty',
            6:'sixty',
            7:'seventy',
            8:'eighty',
            9:'ninety'}
    teens = {11:'eleven',
             12:'twelve',
             13:'thirteen',
             14:'fourteen',
             15:'fifteen',
             16:'sixteen',
             17:'seventeen',
             18:'eighteen',
             19:'nineteen'}
    ones = {0:'',
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine'}

    # num_text stores the word representation of num
    num_text = ''
    
    for i in range(0,len(num)+1):
        # loop through each integer place (starting with largest) and add suffix
        if i == 0:
            # thousands place
            num_text += thousands[int(num[i])] + ' '
        elif i == 1:
            # hundreds place
            num_text += hundreds[int(num[i])] + ' '
        elif i == 2:
            # tens place
            if int(num[-2:]) >= 11 and int(num[-2:]) <= 19:
                # handle number that end with 11 - 19 (inclusive)
                if int(num) > 100:
                    num_text += 'and ' + teens[int(num[-2:])]
                else:
                    num_text += teens[int(num[-2:])]
                return num_text
            elif int(num) > 100 and int(num[-2:]) != 0:
                num_text += 'and ' + tens[int(num[2])] + ' '
            else: 
                num_text += tens[int(num[2])]
        elif i == 3:
            # ones place
            num_text += ones[int(num[3])]
            return num_text



# Body of program

total = 0
num = 115
print(build_number(add_zeros(num,4)).replace(' ',''))
print(len(build_number(add_zeros(num,4)).replace(' ','')))

for i in range(1,1001):
    total += len(build_number(add_zeros(i,4)).replace(' ',''))
    # print(build_number(add_zeros(i,4)))
print(total)
