'''
Write a function that takes as input a n x n 2D array and rotates the array by 90 degrees clockwise 
'''
import typing
import pprint
import copy

def rotate_array(matrix: typing.List[typing.List[int]]) -> typing.List[int] : 
    '''
    observation: when we rotate, rows becomes columns 
    r0 = c4 
    r1 = c3 
    r2 = c2
    ... >> new r0 = r[-1][0], r[-2][0], r[-3][0], ...
    ... >> new r1 = r[-1][1], r[-2][1], r[-4][1], ...

    concept: 
    1. construct a false container of NxN
    1. fill it by walking  through it 
    '''

    rows, cols = len(matrix), len(matrix[0])
    new_matrix = [[0 for i in range(cols)] for j in range(rows)]

    for row in range(rows): 
        for col in range(cols): 
            new_matrix[row][col] = matrix[~col][row]
    
    matrix = copy.deepcopy(new_matrix)
    return matrix 

def rotate_arrayv2(matrix: typing.List[typing.List[int]]) -> typing.List[int] : 
    '''
    implmenting in O(1) space 
    Concept 
    1. Rotate in a layer by layer fashion 
    2. within each layer, echange groups of four elements at a time a = 
    '''
    matrix_size = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(i, matrix_size - i):
            (matrix[i][j],
            matrix[j][~i],
            matrix[~i][~j], 
            matrix[~j][i]) = \
                (matrix[~j][i],
                matrix[i][j],
                matrix[j][~i],
                matrix[~i][~j])

    return matrix 

### TEST CASE 

a = [[i for i in range(10)] for j in range(10)]

pprint.pprint(a) 
pprint.pprint(rotate_array(a))
pprint.pprint(rotate_arrayv2(a))