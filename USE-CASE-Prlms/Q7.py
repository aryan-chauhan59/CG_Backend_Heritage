# Insert multiple employee IDs into a BST and search for a given ID.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
        
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
        
    return root

def search_bst(root, val):
    if not root or root.val == val:
        return root
        
    if val < root.val:
        return search_bst(root.left, val)
        
    return search_bst(root.right, val)

employee_ids = [105, 102, 108, 101, 104, 109]
bst_root = None

for emp_id in employee_ids:
    bst_root = insert_bst(bst_root, emp_id)

search_id = 104
result = search_bst(bst_root, search_id)

print("Searching for Employee ID:", search_id)
if result:
    print("Result: Employee ID", result.val, "Found in BST.")
else:
    print("Result: Employee ID Not Found.")

search_id_missing = 999
result_missing = search_bst(bst_root, search_id_missing)

print("Searching for Employee ID:", search_id_missing)
if result_missing:
    print("Result: Employee ID", result_missing.val, "Found in BST.")
else:
    print("Result: Employee ID Not Found.")