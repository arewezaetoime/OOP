

class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):

        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):

        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class TestCat(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('doncho')

    def test_cat_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_asleep(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == '__main__':
    unittest.main()

import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Kuncho")

    def test_cat_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_asleep(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()