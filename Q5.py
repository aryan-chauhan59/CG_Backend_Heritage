# Petrol Expense Calculator


print("Petrol Expense Calculator")

# Getting inputs
distance = float(input("Enter distance travelled in km: "))
mileage = float(input("Enter vehicle mileage (km per litre): "))
petrol_price = float(input("Enter petrol price per litre: "))

fuel_required = distance / mileage
total_cost = fuel_required * petrol_price

print("\nTravel Summary")
print(f"Distance Travelled: {distance:.2f} km")
print(f"Vehicle Mileage: {mileage:.2f} km/l")
print(f"Fuel Required: {fuel_required:.2f} litres")
print(f"Total Fuel Cost: ${total_cost:.2f}")