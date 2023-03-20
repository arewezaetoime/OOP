from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float or int, fuel_consumption: float or int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle, ABC):
    AIR_CONDITIONER = 0.9

    def drive(self, distance: float) -> None:
        consumption = (self.fuel_consumption + Car.AIR_CONDITIONER) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle, ABC):
    AIR_CONDITIONER = 1.6

    def drive(self, distance: float):
        consumption = (self.fuel_consumption + Truck.AIR_CONDITIONER) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95