

class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



import unittest


class WorkerTest(unittest.TestCase):

    def test_initialization(self):

        worker = Worker('Ivan', 500, 20)
        self.assertEqual(worker.name, 'Ivan')
        self.assertEqual(worker.salary, 500)
        self.assertEqual(worker.energy, 20)

    def test_rest(self):
        worker = Worker('Ivan', 500, 20)
        worker.rest()
        self.assertEqual(worker.energy, 21)

    def test_work(self):
        worker = Worker('Ivan', 500, 0)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_money(self):
        worker = Worker('Ivan', 500, 20)
        worker.work()

        self.assertEqual(worker.money, 500)

    def test_energy(self):
        worker = Worker('Ivan', 400, 20)
        worker.work()

        self.assertEqual(worker.energy, 19)

    def test_get_info(self):
        worker = Worker('Ivan', 50, 50)

        self.assertEqual(worker.get_info(), 'Ivan has saved 0 money.')


if __name__ == '__main__':
    unittest.main()