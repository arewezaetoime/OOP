class Hero:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def __str__(self):
        return f' "{self.name} of type {self.__class__.__name__} has level {self.level}"'
