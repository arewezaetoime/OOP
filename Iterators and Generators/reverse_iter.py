from typing import List, Tuple


class reverse_iter:
    def __init__(self, iterable: List or Tuple):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        # else:
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4, 5])

for i in reversed_list:
    print(i)
