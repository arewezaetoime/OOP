from typing import List


class IntegerList:
    def __init__(self):
        self.list_integers: List[int] = []

    def add(self, element) -> None or ValueError:

        if not isinstance(element, int):
            raise Exception('Instance not integer')

        self.list_integers.append(element)
        return self.list_integers

    def remove_index(self, index: int) -> None or IndexError:

        if 0 <= index < len(self.list_integers):
            self.list_integers.pop(index)
        else:
            raise IndexError()

    def get(self, index: int) -> int or IndexError:

        if 0 <= index < len(self.list_integers):
            raise IndexError()

        return self.list_integers[index]

    def insert(self, index: int) -> (None or IndexError or ValueError):

        if not isinstance(index, int):
            raise ValueError()

        if 0 <= index < len(self.list_integers):
            raise IndexError()

        self.list_integers.insert(index)

    def get_biggest(self):
        return max(self.list_integers)

    def get_index(self, value: int):
        return self.list_integers.index(value)


