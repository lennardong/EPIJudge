from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    '''Concept: build a list for left node, mirror the process for right node. compare'''

    def build_tree (tree: BinaryTreeNode, mirror: bool = False) -> list: 
        '''Returns an inorder list of the binary tree. 

        If mirror = True, returns a mirror
        '''
        #base case 
        if tree is None: 
            return [] 
        left = build_tree(tree.left)
        right = build_tree(tree.right)

        if mirror: 
            return right + [tree.data] + left 

        return left + [tree.data] + right 

    left = build_tree(tree.left)
    right = build_tree(tree.right, True)
    
    print (f'\nleft: {left}')
    print (f'right: {right}')
    print (f'symmetrical: {left == right}')

    return True if left == right else False 

### TEST CASES 
# a = BinaryTreeNode(0)
# a.left = BinaryTreeNode(1) 
# a.left.left = BinaryTreeNode(2) 
# a.left.right = BinaryTreeNode(3)
# a.left.right.left = BinaryTreeNode(6)
# a.left.right.left = BinaryTreeNode(7)
# a.left.left.left = BinaryTreeNode(4)
# a.left.left.right = BinaryTreeNode(5)
# a.left.left.left.left = BinaryTreeNode(8)
# a.left.left.left.right = BinaryTreeNode(9)
# a.left.left.left.left.left = BinaryTreeNode(10) 
# a.left.left.left.left.right = BinaryTreeNode(11)
# # Note: this portion will reveal the false True. 
# a.right = BinaryTreeNode(2) 
# a.right.right = BinaryTreeNode(99) 
# a.right.right.right = BinaryTreeNode(98) 
# a.right.right.right.right = BinaryTreeNode(97) 
# a.right.right.right.right.right = BinaryTreeNode(96) 
# print (is_symmetric(a))

# b = BinaryTreeNode(1)
# b.left = BinaryTreeNode(2)
# b.right = BinaryTreeNode(3)
# b.left.left = BinaryTreeNode(4)
# b.left.right = BinaryTreeNode(5)

# c = BinaryTreeNode(1)
# c.left = BinaryTreeNode(2)
# c.right = BinaryTreeNode(2)
# c.left.left = BinaryTreeNode(3)
# c.right.right = BinaryTreeNode(3)


# print (is_symmetric(b))
# print (is_symmetric(c))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
