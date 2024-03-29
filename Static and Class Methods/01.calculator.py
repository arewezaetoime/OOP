from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums):
        return sum(nums)

    @staticmethod
    def multiply(*args):
        result = reduce(lambda a, b: a * b, args)
        return result

    @staticmethod
    def divide(*args):
        result = reduce(lambda a, b: a / b if a != 0 and b != 0 else a + b, args)
        return result

    @staticmethod
    def subtract(*args):
        result = reduce(lambda a, b: a - b, args)
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))