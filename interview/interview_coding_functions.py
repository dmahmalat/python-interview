import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Car:
    id: str
    make: str
    model: str
    price: int

    # add code here

class CarsCollection(list):
    def __init__(self, cars: List[Car]):
        # add code here

    def sort_cheapest_first(self):
        # add code here

    def sort_most_expensive_first(self):
        # add code here

    def get_cheapest(self):
        # add code here

    def get_most_expensive(self):
        # add code here


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


if __name__ == "__main__":
    unittest.main()
