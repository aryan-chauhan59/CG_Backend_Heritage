# Implement Linear Search to find a target in an unsorted list.

def linear_search(product_ids, target_id):
    for index in range(len(product_ids)):
        if product_ids[index] == target_id:
            return f"Product found at position {index}"
            
    return "Product not found"

unsorted_products = [105, 302, 408, 99, 15]
print(linear_search(unsorted_products, 408))