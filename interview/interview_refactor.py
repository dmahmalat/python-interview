from typing import *
import random


class Sedan:
    wheels = 4

    def __init__(self, model: str, weight: float, power: int, value: float):
        self.model = model
        self.weight = weight
        self.power = power
        self.value = value

    def max_speed(self):
        return self.weight * self.power

    def time_to_stop(self, current_speed: float):
        return current_speed / self.weight / self.wheels


class SportsCar:
    wheels = 4

    def __init__(self, model: str, weight: float, power: int, value: float):
        self.model = model
        self.weight = weight
        self.power = power
        self.value = value

        self.wheels = 4

    def max_speed(self):
        return self.weight * self.power

    def time_to_stop(self, current_speed: float):
        return current_speed / self.weight / self.wheels


class ElectricCar:
    wheels = 4

    def __init__(self, model: str, weight: float, power: int, value: float):
        self.model = model
        self.weight = weight
        self.power = power
        self.value = value

        self.wheels = 4

    def max_speed(self):
        return self.weight * self.power

    def time_to_stop(self, current_speed: float):
        return current_speed / self.weight / self.wheels


class MotorBike:
    wheels = 2

    def __init__(self, model: str, weight: float, power: int, value: float):
        self.model = model
        self.weight = weight
        self.power = power
        self.value = value

    def max_speed(self) -> float:
        return (self.weight * self.power) ** 2

    def time_to_stop(self, current_speed: float) -> float:
        return current_speed / self.weight / self.wheels

    def do_wheelie(self) -> None:
        return print("Doing a wheelieee!")


def collision_damage(
    x: Union[Sedan, SportsCar, ElectricCar, MotorBike],
    y: Union[Sedan, SportsCar, ElectricCar, MotorBike],
) -> float:
    if isinstance(x, Sedan) and isinstance(y, MotorBike):
        return x.value * 0.50 + y.value * 1.0
    elif isinstance(x, ElectricCar) and isinstance(y, MotorBike):
        return x.value * 0.50 + y.value * 1.0
    elif isinstance(x, SportsCar) and isinstance(y, MotorBike):
        return x.value * 0.50 + y.value * 1.0
    elif isinstance(x, MotorBike) and isinstance(y, Sedan):
        return x.value * 1.0 + y.value * 0.5
    elif isinstance(x, MotorBike) and isinstance(y, ElectricCar):
        return x.value * 1.0 + y.value * 0.5
    elif isinstance(x, MotorBike) and isinstance(y, SportsCar):
        return x.value * 1.0 + y.value * 0.5

    elif isinstance(x, Sedan) and isinstance(y, Sedan):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, Sedan) and isinstance(y, ElectricCar):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, Sedan) and isinstance(y, SportsCar):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, SportsCar) and isinstance(y, SportsCar):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, SportsCar) and isinstance(y, ElectricCar):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, SportsCar) and isinstance(y, Sedan):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, ElectricCar) and isinstance(y, SportsCar):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, ElectricCar) and isinstance(y, Sedan):
        return x.value * 0.3 + y.value * 0.3
    elif isinstance(x, ElectricCar) and isinstance(y, ElectricCar):
        return x.value * 0.3 + y.value * 0.3

    elif isinstance(x, MotorBike) and isinstance(y, MotorBike):
        return x.value * 1.0 + y.value * 1.0


def generate_licence_plate(x: Union[Sedan, SportsCar, ElectricCar, MotorBike]) -> str:
    if x.wheels == 4:
        return (
            f"FOUR{random.randint(1, 10)}{random.randint(1, 10)}{random.randint(1, 10)}"
        )
    else:
        return (
            f"TWO{random.randint(1, 10)}{random.randint(1, 10)}{random.randint(1, 10)}"
        )

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
