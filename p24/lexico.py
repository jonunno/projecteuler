import numpy as np


arr = [1,2,3,4]

def permute(arr):
    if (len(arr) == 2):
        return [ arr[1], arr[0] ]
    
    # if array is decreasing, return it in reverse order

print(permute([0,1]))

def permutes(arr1, arr2):
    """
    let k equal last value in array 1

    if array 2 descending:
        if k > first value in arr[2] (i.e. k is larger than any value in array 2)
            - pop last element of array 1
            - let array 2 = [k] + [array 2]
            - let k = last element of array 1
            - reverse array 2
            - swap k with first element in array 2 greater than k
            - permuate(arr1 , arr2) 
        else:
            - reverse array 2     
            - find the smallest number in array 2 that's greater than k
            - swap that number with k
            - then permute array 1 and array 2 again


    if length of array 2 = 2, then swap array 2
    then call permute on array 1 and 2 again 
    """
    # check if array 2 is descending



def swap([a,b]):