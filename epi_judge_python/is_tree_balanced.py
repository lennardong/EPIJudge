from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    print(
        f'''
        Tree: {tree}
        Data: {tree.data}
        Left: {tree.left}
        Right: {tree.right}''')

    balanced_status_w_height = collections.namedtuple(
        'balanced_status', ['balanced' 'height'])

    depth = 0 
    while tree: 
        print (f'\ndepth:  {depth}\ndata:   {tree.data}\nleft:   {tree.left}')
        tree = tree.left
        depth += 1 

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
