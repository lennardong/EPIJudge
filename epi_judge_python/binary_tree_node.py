from test_framework.binary_tree_utils import (binary_tree_to_string,
                                              equal_binary_trees)


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()


## TESTING 
'''
a = BinaryTreeNode(1,None,None)
b = BinaryTreeNode(2,a,list('goodbye'))
print (f'a str:             {a}')
print (f'a type:            {type(a)}')
print (f'a str.left:        {a.left}')
print (f'a type.left:       {type(a.left)}')
# print (f'b str: {b}')
print (f'b type:            {type(b)}')
print (f'b str.left:        {b.left}')
print (f'b type.left:       {type(b.left)}')
print (f'b type.left.left:  {type(b.left.left)}')
print (f'b type.right:      {type(b.right)}')
'''