# Mobile Recharge Bill Generator

print("--- Mobile Recharge Bill Generator ---")

# Getting inputs
customer_name = input("Enter Customer Name: ")
mobile_number = input("Enter Mobile Number: ")
recharge_amount = float(input("Enter Base Recharge Amount: ₹"))

gst_amount = recharge_amount * 0.18  
total_payable = recharge_amount + gst_amount

print("\n--- Payment Receipt ---")
print(f"Customer: {customer_name}")
print(f"Mobile No: {mobile_number}")
print(f"Base Recharge: ₹{recharge_amount:.2f}")
print(f"GST (18%): ₹{gst_amount:.2f}")
print("-" * 25)
print(f"Total Payable: ₹{total_payable:.2f}")