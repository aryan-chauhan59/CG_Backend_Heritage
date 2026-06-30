# Create a Binary Tree and calculate its height.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def get_height(root):
    if not root:
        return 0
    
    return 1 + max(get_height(root.left), get_height(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6) 

print("Tree Height:", get_height(root))