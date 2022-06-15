'''
Replace each 'a' by 2 d's 
Delete each entry containing a 'b'

'''
import typing


def replace_and_remove(arr: list, stop_point: int) -> list: 
    '''
    1. iterate through list
    2. if a, extend with d, d
    3. if b, remove 
    for code consistency, use slicing 
    '''
    idx = 0 
    while idx <= stop_point: 
        if arr[idx] == 'a':  #double D
            arr = arr[:idx] + list('dd') + arr[idx + 1:]
            idx += 1 
        elif arr[idx] == 'b':  #remove B 
            arr = arr[:idx] + arr[idx + 1:]
        else:
            idx += 1 
        print (arr, ':', idx, ':', arr[idx])
            
    return arr 



## TEST CASES 
a = list('abacsedd')
print (replace_and_remove(a,4), 'ddddc...')