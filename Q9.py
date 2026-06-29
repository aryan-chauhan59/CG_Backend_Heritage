#   Movie Ticket Booking System


print("Movie Ticket Booking System")


customer_name = input("Enter Customer Name: ")
num_tickets = int(input("Enter Number of Tickets: "))
price_per_ticket = float(input("Enter Price Per Ticket: ₹"))

base_amount = num_tickets * price_per_ticket
booking_charge = 50.00  
final_bill = base_amount + booking_charge

print("\nBooking Summary")
print(f"Customer Name: {customer_name}")
print(f"Tickets Booked: {num_tickets}")
print(f"Base Ticket Cost: ₹{base_amount:.2f}")
print(f"Online Booking Charge: ₹{booking_charge:.2f}")
print("-" * 25)
print(f"Final Bill: ₹{final_bill:.2f}")