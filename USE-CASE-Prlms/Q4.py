# Check whether two Binary Trees are identical.

def is_identical(p, q):
    if not p or not q: 
        return p == q
    return p.val == q.val and is_identical(p.left, q.left) and is_identical(p.right, q.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(1, TreeNode(2), TreeNode(4))

print("Tree 1 & Tree 2 Identical?", is_identical(tree1, tree2))
print("Tree 1 & Tree 3 Identical?", is_identical(tree1, tree3))
print("-" * 30)