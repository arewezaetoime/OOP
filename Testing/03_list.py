from typing import List


class IntegerList:
    def __init__(self, integer: int):
        self.integer = integer
        self.list_integers: List[int] = []

    def add(self, element: int) -> None or ValueError:

        if not isinstance(element, int):
            raise ValueError()

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


from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_values_list = IntegerList(5)

    def test_add_integer_class(self):
        self.integer_values_list.add(4)

        self.assertListEqual(self.integer_values_list.add(4), [4, 4])

    def test_remove_index_value(self):
        self.integer_values_list.remove_index(4)
        self.assertListEqual(self.integer_values_list.remove_index(0), [4])

if __name__ == '__main__':
    main()

