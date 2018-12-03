# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:21:29 2018

@author: Jon

ProjectEuler.net

Problem 17

---
Progress
    2018-11-24 ()
    2018-11-25

"""




def write_ones(numbers_dic, prefix, prefix_int, ones):
    """ returns dictionary with written increments in the ones place """
    for num in ones:
        numbers_dic[prefix_int + num] = prefix + ones[num]
    return numbers_dic

def write_tens(dic, prefix, prefix_int, tens, ones):
    """ returns dictionary with written increments in the tens place """
    for key,value in tens.items():
        if key == 10:
            pass
        else:
            write_ones(numbers,prefix + 'and' + value,key+prefix_int,ones)



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

tens = {0:'',
        10:'ten',
        20:'twenty',
        30:'thirty',
        40:'forty',
        50:'fifty',
        60:'sixty',
        70:'seventy',
        80:'eighty',
        90:'ninety'}

hundreds = {0:'',
            100:'onehundred',
            200:'twohundred',
            300:'threehundred',
            400:'fourhundred',
            500:'fivehundred',
            600:'sixhundred',
            700:'sevenhundred',
            800:'eighthundred',
            900:'ninehundred'}

numbers = {0:'',
           1:'one',
           2:'two',
           3:'three',
           4:'four',
           5:'five',
           6:'six',
           7:'seven',
           8:'eight',
           9:'nine',
           10:'ten',
           11:'eleven',
           12:'twelve',
           13:'thirteen',
           14:'fourteen',
           15:'fifteen',
           16:'sixteen',
           17:'seventeen',
           18:'eighteen',
           19:'nineteen'}


for key, value in hundreds.items():
    write_tens(numbers,value,key,tens,ones)




