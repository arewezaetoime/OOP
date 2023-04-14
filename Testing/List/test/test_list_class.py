from unittest import TestCase, main
from project.list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_values_list = IntegerList()

    def test_add_integer_class(self):
        with self.assertRaises(Exception) as er:
            self.integer_values_list.add('3')

        self.assertEqual('Instance not integer', er.exception)

    def test_append_element_to_the_list(self):



if __name__ == '__main__':
    main()