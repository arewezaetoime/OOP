from project.beverage import HotBeverage


class Coffee(HotBeverage):
    def __init__(self, name: str, price: float, caffeine: float):
        super().__init__(name, price)
        self.__caffeine = caffeine

