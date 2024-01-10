from unreliable_car import UnreliableCar  # unreliable_car.py

# 50% reliability
my_unreliable_car = UnreliableCar('Unreliable 50', 100, 50)

for i in range(10):
    distance_driven = my_unreliable_car.drive(10)
    print(f"Attempt {i+1}: Tried to drive 10km, drove {distance_driven}km")

print(my_unreliable_car)
