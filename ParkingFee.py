print("===== Parking Fee Calculator =====")

vehicle = input("Enter vehicle type (Bike/Car): ").lower()

hours = float(input("Enter parking duration (hours): "))

if vehicle == "bike":
    rate = 10

elif vehicle == "car":
    rate = 20

else:
    print("Invalid vehicle type")
    exit()

fee = rate * hours

print(f"\nVehicle Type: {vehicle.title()}")
print(f"Parking Duration: {hours} hours")
print(f"Total Fee = ₹{fee}")