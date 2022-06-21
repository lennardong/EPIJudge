class BinaryTreeNode(): 
    def __init__(self, data = None, left = None, right = None):
        self.data = data 
        self.left = left 
        self.right = right 
    

def traverse_tree_inorder(tree: BinaryTreeNode) -> list: 
    '''Concept: traverse a binary tree

    Preorder = Root, Left, Right
    Inorder = Left, Root, Right 
    Postorder = Left, Right, Root
    '''
    #base case 
    if tree is None:
        return None
    
    #reducing case 
    left = traverse_tree_inorder(tree.left)
    print (left.data)
    if not left:
        return ([tree.data].append(traverse_tree_inorder(tree.left)) )
    right = traverse_tree_inorder(tree.right)
    print (right.data)
    if not right:
        return ([tree.data].append(traverse_tree_inorder(tree.right)) )


def inorder(root: BinaryTreeNode) -> list :
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)

def traversal(tree: BinaryTreeNode, form: int) -> list:
    if tree is None: 
        return [] 

    left_list = traversal(tree.left, form)
    right_list = traversal(tree.right, form)
    
    if form == 1:  #preorder
        return [tree.data] + left_list + right_list 
    if form == 2: #inorder 
        return left_list + [tree.data] + right_list 
    if form == 3: #postorder 
        return left_list + right_list + [tree.data]


### TEST CASES 
a = BinaryTreeNode(0)
a.left = BinaryTreeNode(1) 
a.left.left = BinaryTreeNode(2) 
a.left.right = BinaryTreeNode(3)
a.left.right.left = BinaryTreeNode(6)
a.left.right.left = BinaryTreeNode(7)
a.left.left.left = BinaryTreeNode(4)
a.left.left.right = BinaryTreeNode(5)
a.left.left.left.left = BinaryTreeNode(8)
a.left.left.left.right = BinaryTreeNode(9)
a.left.left.left.left.left = BinaryTreeNode(10) 
a.left.left.left.left.right = BinaryTreeNode(11)
# Note: this portion will reveal the false True. 
a.right = BinaryTreeNode(2) 
a.right.right = BinaryTreeNode(99) 
a.right.right.right = BinaryTreeNode(98) 
a.right.right.right.right = BinaryTreeNode(97) 
a.right.right.right.right.right = BinaryTreeNode(96) 

print (a)
print (traversal(a, 1))
print (traversal(a, 2))
print (traversal(a, 3))

b = BinaryTreeNode(1)
b.left = BinaryTreeNode(2)
b.right = BinaryTreeNode(3)
b.left.left = BinaryTreeNode(4)
b.left.right = BinaryTreeNode(5)

print (b)
print (traversal(b, 2))
print (inorder(b))
# print (traverse_tree_inorder(b))
# preoder: 1 2 4 5 3
# inorder: 4 2 5 1 3
# postoder: 4 5 2 3 1

