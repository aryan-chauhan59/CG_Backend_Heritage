# Find the minimum and maximum values in a BST.

def get_min(root):
    while root and root.left: 
        root = root.left
    return root.val if root else None

def get_max(root):
    while root and root.right: 
        root = root.right
    return root.val if root else None
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
num_tree = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, None, TreeNode(20)))

print("Minimum Value:", get_min(num_tree))
print("Maximum Value:", get_max(num_tree))