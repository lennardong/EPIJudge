from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    
    balanced_status_w_height = collections.namedtuple(
        'balanced_status', ['balanced', 'height'])

    def check_balanced(tree):
        # Basecase
        # is a leaf. If so, it is balanced (0,0) and height = -1
        if not tree:
            return balanced_status_w_height(True, -1)
        
        # Recursive Function (reducing layer): 
        # walk L, R
        left_branch = check_balanced(tree.left)
        right_branch = check_balanced(tree.right) 
        
        # Base Case #02 
        # If its imbalanced, bubble it up
        if not left_branch.balanced: 
            return left_branch
        if not right_branch.balanced: 
            return right_branch

        # Recursive Function (computation)
        # check for balanced and height. This is the interaction between frames
        is_balanced = abs(left_branch.height - right_branch.height) <= 1 
        height = max(left_branch.height, right_branch.height) + 1 
        # print (f'[DEBUG] is_balanced: {is_balanced} | height: {height}...   {tree}')
        
        # Recursive Function (return)
        return balanced_status_w_height(is_balanced, height)
    
    is_bal = check_balanced(tree).balanced 
    # print ('[DEBUG] RETURN: ', is_bal) #🐞 DEBUG
    return is_bal

### TEST CASE 
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
# Note: this portion will reveal the false True. 
# a.right = BinaryTreeNode(2) 
# a.right.right = BinaryTreeNode(99) 
# a.right.right.right = BinaryTreeNode(98) 
# a.right.right.right.right = BinaryTreeNode(97) 
# a.right.right.right.right.right = BinaryTreeNode(96) 

# print (a)
# print (is_balanced_binary_tree(a))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
