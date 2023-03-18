# class Cat:
#     def sound(self):
#         return 'cat'
#
#
# class Dog:
#     def sound(self):
#         return 'dog'
#
#
# for any_type in Cat(), Dog():
#     print(any_type.sound())

class Shape:
    def calculate_area(self):
        return None


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 2

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


triangle = Triangle()
square = Square()

for area in triangle, square:
    print(area.calculate_area())
