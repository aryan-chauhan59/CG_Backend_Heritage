# Build a Binary Tree from a list and print its inorder traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build_tree(arr, i=0):
    if i < len(arr) and arr[i] is not None:
        return TreeNode(arr[i], build_tree(arr, 2*i + 1), build_tree(arr, 2*i + 2))
    return None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

arr = [1, 2, 3, 4, 5, 6, 7]
print("Inorder Traversal:")
inorder(build_tree(arr))
print()