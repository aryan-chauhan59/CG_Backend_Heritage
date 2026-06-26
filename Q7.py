# Hotel Room booking calculator

print("Hotel Room Booking Calculator")

guest_name = input("Enter Guest Name: ")
nights = int(input("Enter Number of Nights: "))
cost_per_night = float(input("Enter Cost Per Night: $"))

room_charge = nights * cost_per_night
gst = room_charge * 0.12  # 12% GST
final_amount = room_charge + gst

print("\n Hotel Invoice")
print(f"Guest Name: {guest_name}")
print(f"Duration of Stay: {nights} night(s)")
print(f"Base Room Charge: ${room_charge:.2f}")
print(f"GST (12%): ${gst:.2f}")
print("-" * 25)
print(f"Final Amount Due: ${final_amount:.2f}")