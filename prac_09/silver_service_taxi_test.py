from silver_service_taxi import SilverServiceTaxi

luxury_taxi = SilverServiceTaxi("Luxury One", 100, 2)

# Drive the taxi
luxury_taxi.drive(18)

print(luxury_taxi)
print(f"Total fare: ${luxury_taxi.get_fare():.2f}")
