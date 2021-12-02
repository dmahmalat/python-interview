# Imports =============================================================================
import unittest
from dataclasses import dataclass
from typing import List

# Class definitions ===================================================================
@dataclass
class Car:
    id: str
    make: str
    model: str
    price: int

    # Override __repr__ to match the test case formatting
    def __repr__(self):
        key_value_list = [f"{key}={value}" for key, value in self.__dict__.items()]
        return "{}".format(' '.join(key_value_list))

# Extending the list pre-built object
class CarsCollection(list):
    def sort_cheapest_first(self) -> None:
        self.sort(key=lambda c: c.price)

    def sort_most_expensive_first(self) -> None:
        self.sort(key=lambda c: c.price, reverse=True)

    # Do not alter the list while getting the correct items
    def get_cheapest(self) -> Car:
        sorted_list = sorted(self, key=lambda c: c.price)
        return sorted_list[0]

    def get_most_expensive(self) -> Car:
        sorted_list = sorted(self, key=lambda c: c.price, reverse=True)
        return sorted_list[0]

# Code left intact for validation =====================================================
class TestCarsCollection(unittest.TestCase):
    tesla = Car(id="1", make="Tesla", model="Model 3", price=45000)
    civic = Car(id="2", make="Honda", model="Civic", price=22000)
    lamborghini = Car(id="3", make="Lamborghini", model="Aventador", price=250000)

    def setUp(self) -> None:
        self.collection = CarsCollection([self.civic, self.tesla, self.lamborghini])

    def test_sort_cheapest_first(self) -> None:
        self.collection.sort_cheapest_first()
        self.assertListEqual(list1=self.collection, list2=[self.civic, self.tesla, self.lamborghini])

    def test_sort_most_expensive_first(self) -> None:
        self.collection.sort_most_expensive_first()
        self.assertListEqual(list1=self.collection, list2=[self.lamborghini, self.tesla, self.civic])

    def test_get_cheapest(self) -> None:
        self.assertEqual(first=self.collection.get_cheapest(), second=self.civic)

    def test_get_most_expensive(self) -> None:
        self.assertEqual(first=self.collection.get_most_expensive(), second=self.lamborghini)

    def test_repr(self):
        self.assertEqual(first=self.civic.__repr__(), second="id=2 make=Honda model=Civic price=22000")


def main():
    # Context module required to discover the correct TestCase classes
    unittest.main(module=__name__, exit=False)

if __name__ == "__main__":
    main()
