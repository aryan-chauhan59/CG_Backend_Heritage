class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
#1)
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# 2)
def search(root, val):
    if root is None:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)

# 3)
def delete(root, val):
    if root is None:
        return root
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.left is None: return root.right
        if root.right is None: return root.left
        
        temp = root.right
        while temp.left:
            temp = temp.left
            
        root.val = temp.val
        root.right = delete(root.right, temp.val)
        
    return root

# 4)
def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]

tree = None
for num in [50, 30, 70, 20, 40, 60, 80, 35]:
    tree = insert(tree, num)

print("Is 40 in tree?", search(tree, 40))
print("Is 99 in tree?", search(tree, 99))

print("\nBefore Deleting")
print("Inorder:  ", inorder(tree))
print("Preorder: ", preorder(tree))
print("Postorder:", postorder(tree))

tree = delete(tree, 30)

print("\nAfter Deleting 30")
print("Inorder:  ", inorder(tree))
print("Preorder: ", preorder(tree))
print("Postorder:", postorder(tree))

# OUTPUT:

# Is 40 in tree? True
# Is 99 in tree? False

# Before Deleting
# Inorder:   [20, 30, 35, 40, 50, 60, 70, 80]
# Preorder:  [50, 30, 20, 40, 35, 70, 60, 80]
# Postorder: [20, 35, 40, 30, 60, 80, 70, 50]

# After Deleting 30
# Inorder:   [20, 35, 40, 50, 60, 70, 80]
# Preorder:  [50, 35, 20, 40, 70, 60, 80]
# Postorder: [20, 40, 35, 60, 80, 70, 50]