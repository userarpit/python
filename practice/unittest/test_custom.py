import unittest


class CustomTestCase(unittest.TestCase):
    def assertAllIntegers(self, values):
        for value in values:
            self.assertIsInstance(
                value,
                int,
            )

    def assertNotAllIntegers(self, values):
        for value in values:
            self.assertNotIsInstance(value, int)


class TestIntegerList(CustomTestCase):
    def test_values_are_integers(self):
        integer_list = [1, 2, 3, 4, 5]
        self.assertAllIntegers(integer_list)

    def test_values_are_not_integers(self):
        _list = [2.6, "hello"]
        self.assertNotAllIntegers(_list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
