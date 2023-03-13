from project.animal import Animal


class Cheetah(Animal):
    MONEY_TO_BE_CARED = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Cheetah.MONEY_TO_BE_CARED)

