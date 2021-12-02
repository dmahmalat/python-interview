# Imports =============================================================================
from abc import ABC, abstractmethod # Abstract classes
from typing import *
import random

# Define an abstract class ============================================================
class Vehicle(ABC):
    def __init__(self, model: str, weight: float, power: int, value: float):
        self.model = model
        self.weight = weight
        self.power = power
        self.value = value
        super().__init__()
    
    # Shared properties
    @property
    @abstractmethod
    def wheels(self):
        pass

    # Shared methods
    def max_speed(self):
        return self.weight * self.power

    def time_to_stop(self, current_speed: float):
        return current_speed / self.weight / self.wheels

    def generate_license_plate(self):
        prefix = "FOUR" if self.wheels == 4 else "TWO"
        return (
                f"{prefix}{random.randint(1, 10)}{random.randint(1, 10)}{random.randint(1, 10)}"
            )

    def collision_damage(self, v: "Vehicle"):
        # Initialize damage factor according to
        # whether we are on 4 or 2 wheels
        a = 0.3 if self.wheels == 4 else 1
        b = 0.3 if v.wheels == 4 else 1

        # If vehicles with different wheel types collide,
        # the damage factor of the 4 wheelers changes from 0.3 to 0.5
        if a != b:
            a = 0.5 if a == 0.3 else a
            b = 0.5 if b == 0.3 else b

        return a * self.value + b * v.value

# Class definitions ===================================================================
class Sedan(Vehicle):
    wheels = 4

class SportsCar(Vehicle):
    wheels = 4

class ElectricCar(Vehicle):
    wheels = 4

class MotorBike(Vehicle):
    wheels = 2

    def max_speed(self) -> float:
        return super().max_speed() ** 2

    def do_wheelie(self) -> None:
        return print("Doing a wheelieee!")

# Method definitions ==================================================================
def collision_damage(x: Vehicle, y: Vehicle) -> float:
    return x.collision_damage(y)

def generate_licence_plate(v: Vehicle) -> str:
    return v.generate_license_plate()

# Code left intact for validation =====================================================
def main():
    one = Sedan(model="toyota", weight=5000.0, power=150, value=10500.0)
    two = SportsCar(model="Nissan", weight=4000.0, power=250, value=30000.0)
    three = ElectricCar(model="dodge", weight=5000.0, power=200, value=20000.0)
    four = MotorBike(model="bmw", weight=500.0, power=150, value=5000.0)

    assert collision_damage(one, two) == 12150.0
    assert collision_damage(two, one) == 12150.0
    assert collision_damage(three, one) == 9150.0
    assert collision_damage(one, three) == 9150.0
    assert collision_damage(two, three) == 15000.0
    assert collision_damage(three, two) == 15000.0
    assert collision_damage(two, three) == 15000.0
    assert collision_damage(three, two) == 15000.0
    assert collision_damage(three, four) == 15000.0
    assert collision_damage(four, three) == 15000.0
    assert collision_damage(four, four) == 10000.0

    assert one.max_speed() == 750000.0
    assert two.max_speed() == 1000000.0
    assert three.max_speed() == 1000000.0
    assert four.max_speed() == 5625000000.0

    assert one.time_to_stop(current_speed=100) == 0.005
    assert two.time_to_stop(current_speed=100) == 0.00625
    assert three.time_to_stop(current_speed=100) == 0.005
    assert four.time_to_stop(current_speed=100) == 0.1

    assert "FOUR" in generate_licence_plate(one)
    assert "FOUR" in generate_licence_plate(two)
    assert "FOUR" in generate_licence_plate(three)
    assert "TWO" in generate_licence_plate(four)

    four.do_wheelie()

if __name__ == "__main__":
    main()
