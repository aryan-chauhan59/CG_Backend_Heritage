# Invert (mirror) a Binary Tree.

def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)

tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

print("Original Tree (Inorder):", end=" ")
print_inorder(tree)
print("\nInverted Tree (Inorder):", end=" ")
print_inorder(invert_tree(tree))
print("\n" + "-" * 30)