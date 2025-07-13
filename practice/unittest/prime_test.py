import unittest
from prime_v1 import is_prime


class TestIsPrime(unittest.TestCase):
    def test_check_prime(self):
        for number in [2, 3, 5, 7, 11, 13]:
            with self.subTest(number=number):
                self.assertTrue(is_prime(number))

    def test_check_non_prime(self):
        for number in [4, 6, 8, 15, 21, 12]:
            # breakpoint()
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_prime("5")

    def test_value_error_less_than_two(self):
        for number in [-1, 0, 1]:
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    is_prime(number)

    def test_invalid_type_float(self):
        with self.assertRaises(TypeError):
            is_prime(4.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
