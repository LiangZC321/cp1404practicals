import random
from car import Car  # Import the Car class from car.py

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):

        super().__init__(name, fuel)
        self.reliability = reliability

