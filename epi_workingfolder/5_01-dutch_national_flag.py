'''
Write a program that takes an array A and and index i into A 
It rearranges the elements so that all elements smaller than A[i] appear first
'''

def dutch_flag_partition(A: list, idx: int) -> list: 
    '''
    create 4 subarrays: 
    1. bottom array : smaller than pivot 
    2. middle : equal to pivot 
    3. unclassified : unknown and implicit
    4. top array: larger than pivot 

    the incoming unclassified element will be: idx_equal
    '''
    idx_smaller, idx_equal, idx_larger = 0, 0, len(A)
    
    pivot = A[idx]
    A[idx] = str(A[idx]) + '*'
    print (f'pivot: {pivot}, A[idx]: {A[idx]}')

    while idx_equal < idx_larger: 
        print (f'idx_equal: {idx_equal} | {A}')
        if idx_equal == idx: 
            idx_equal += 1 
        elif A[idx_equal] < pivot: #if smaller, move to back and enlarge idx_smaller and progress forward
            A[idx_smaller], A[idx_equal] = A[idx_equal], A[idx_smaller]
            idx_equal += 1 
            idx_smaller += 1 
        elif A[idx_equal] > pivot: #if larger, enlarge idx_larger and swap spots 
            idx_larger -= 1 
            A[idx_equal], A[idx_larger] = A[idx_larger], A[idx_equal]
        elif A[idx_equal] == pivot: #if equal, enlarge idx_equal
            idx_equal += 1 

    return A 

### TEST CASES 
a = [int(i) for i in list('323423543432')]
print (a)
print (dutch_flag_partition(a, 3))

