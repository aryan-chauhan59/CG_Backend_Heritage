# Find the lowest common ancestor (LCA) of two nodes in a BST.

def lca(root, p, q):
    if not root: 
        return None
    if root.val > max(p.val, q.val): 
        return lca(root.left, p, q)
    if root.val < min(p.val, q.val): 
        return lca(root.right, p, q)
    return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
bst = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
node_p = bst.left          
node_q = bst.left.right    

print("LCA of", node_p.val, "and", node_q.val, "is:", lca(bst, node_p, node_q).val)
print("-" * 30)