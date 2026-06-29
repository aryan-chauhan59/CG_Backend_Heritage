# Shopping Bill Generator


print("Shopping Bill Generator")

product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price_per_unit = float(input("Enter price per unit: "))

total_cost = quantity * price_per_unit
gst = total_cost * 0.18  
final_bill = total_cost + gst

print("\nProfessional Invoice")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per Unit: ${price_per_unit:.2f}")
print(f"Total Base Cost: ${total_cost:.2f}")
print(f"GST (18%): ${gst:.2f}")
print("-" * 28)
print(f"Final Bill: ${final_bill:.2f}")