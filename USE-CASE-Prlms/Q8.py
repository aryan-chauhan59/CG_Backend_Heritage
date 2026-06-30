# Delete a product ID from a BST while maintaining BST properties.

from Q5 import print_inorder


def delete_node(root, key):
    if not root: 
        return None
    if key < root.val: 
        root.left = delete_node(root.left, key)
    elif key > root.val: 
        root.right = delete_node(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        
        curr = root.right
        while curr.left: 
            curr = curr.left
            
        root.val = curr.val
        root.right = delete_node(root.right, root.val)
    return root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
prod_tree = TreeNode(50, TreeNode(30, TreeNode(20), TreeNode(40)), TreeNode(70, TreeNode(60), TreeNode(80)))


print("Before Deleting 30:", end=" ")
print_inorder(prod_tree)
prod_tree = delete_node(prod_tree, 30)
print("\nAfter Deleting 30: ", end=" ")
print_inorder(prod_tree)
print("\n" + "-" * 30)