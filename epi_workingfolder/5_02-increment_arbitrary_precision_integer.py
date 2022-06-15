'''
Write a program which taks as an input an array of digits encoding a non-negative decimal integer and updates the array to represent the integer D+1. 
For example: if the input is <1,2,9>, then you should update the array to <1,3,0> 
'''
from typing import *

def plus_one(A: List[int]) -> List[int]: 
    '''
    work with this digit by digit. 
    if digit == 10, carryover 
    '''
    A[-1] += 1 #add 1 to last item
    for i in reversed(range(len(A))):  #walk from back to front... using index
        if A[i] != 10: #once there are no more carry-forwards, break out of the loop and proceed
            break 
        elif i == 0 and A[i] == 10: #if carryforward goes to the end 
            A[0] = 1
            A.append(0) #Slow Way: A.insert(0,0)
        else: #all other cases 
            A[i], A[i-1] = 0, A[i-1] + 1 
    return A

### TEST CASES
print (plus_one([1,9,9])) # >>> [1,8,0]
print (plus_one([9,9,9,9])) # >>> [9,9,9,9]