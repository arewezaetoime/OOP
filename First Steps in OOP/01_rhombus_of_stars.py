class Rhombus:

    def __init__(self, size: int):
        self.size = size

    # def print_func(self, space, stars):
    #     print(' ' * space + '*' * stars + ' ' * space)

    def draw(self):
        our_figure = []

        for line in range(self.size):
            space_data = self.size - line - 1
            start_data = line + 1
            our_figure.append(' ' * space_data + '* ' * start_data)

        for line in range(self.size - 2, - 1, -1):
            space_data = self.size - line - 1
            start_data = line + 1
            our_figure.append(' ' * space_data + '* ' * start_data)

        return '\n'.join(our_figure)

# rhombus = Rhombus(3)
# rhombus2 = Rhombus(5)
# print(rhombus2.draw())
# print(rhombus.draw())
