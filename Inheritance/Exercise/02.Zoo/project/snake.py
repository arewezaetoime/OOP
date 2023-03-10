from project.lizard import Lizard
from project.mammal import Mammal
from project.reptile import Reptile


class Snake(Reptile):
    def __init__(self, name: str):
        super().__init__(name)


