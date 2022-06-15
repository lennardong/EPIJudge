'''
Write a program that takes two arrays representing integers and returns an array with integer representing their product.
e.g. 
<1,2> x <2> => <2,4> 
'''

from typing import * 

def mult_two_array(A: List[int], B: List[int]) -> List[int]: 
    '''
    example: 32*9 = [3][18] -> [27+1][8] -> [2][8][8]

    1. work in reverse 
    2. while digits are mulipliable, multiply the number together, if >10, carry over 
    3. after digits are exhauseted, complete carryover ifs [i] != 10 
    '''
    res = [0]
    for i in reversed(range(min([len(A), len(B)]))): 
        mult = A[i] * B[i]
        res[-1] = res[-1] + mult % 10
        
        if res[-1] > 10 or mult > 10: 
            res.append(mult // 10 + res[-1] // 10) #things to carry forward 
            res[-2] = res[-1] % 10 #things to keep
        
    
    return list(reversed(res))

### TEST CASES 
print (mult_two_array([12], [14]))
print (mult_two_array([32], [9]))

        

