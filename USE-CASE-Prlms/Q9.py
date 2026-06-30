# Validate whether a given Binary Tree is a valid BST.

def is_valid_bst(root, min_v=float('-inf'), max_v=float('inf')):
    if not root: 
        return True
    if not (min_v < root.val < max_v): 
        return False
    return is_valid_bst(root.left, min_v, root.val) and is_valid_bst(root.right, root.val, max_v)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
valid_bst = TreeNode(2, TreeNode(1), TreeNode(3))
invalid_bst = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))


print("Is Tree 1 a Valid BST?", is_valid_bst(valid_bst))
print("Is Tree 2 a Valid BST?", is_valid_bst(invalid_bst))
print("-" * 30)