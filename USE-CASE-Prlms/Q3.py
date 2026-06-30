# Count the number of leaf nodes in a Binary Tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def count_leaves(root):
    if not root:
        return 0
        
    if not root.left and not root.right:
        return 1
        
    return count_leaves(root.left) + count_leaves(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Leaf Nodes Count:", count_leaves(root))