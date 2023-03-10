class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: [float, int] = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometres: [float, int]):
        if self.fuel - kilometres * self.fuel_consumption >= 0:
            self.fuel -= kilometres * self.fuel_consumption
