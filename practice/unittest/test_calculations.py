import unittest
import argparse
from calculations import (
    add,
    sub,
    mul,
    div,
    mean,
    median,
    mode,
)


class TestArithmeticOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(-1, 5), -6)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 1), -1)

    def test_div(self):
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(-1, 1), -1)
        self.assertRaises(ZeroDivisionError, div, 1, 0)


class TestStatisticalOperations(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6]), 3.5)

    def test_median_odd(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9]), 6)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9]), 4.5)

    def test_median_unsorted(self):
        self.assertEqual(median([7, 1, 3, 3, 2, 6]), 3)

    def test_mode_single(self):
        self.assertEqual(mode([1, 2, 2, 3, 4, 4, 4, 5]), [4])

    def test_mode_multiple(self):
        self.assertEqual(set(mode([1, 1, 2, 3, 4, 4, 5, 6])), {1, 4})


def make_arithmetic_suite():
    arithmetic_suite = unittest.TestSuite()
    arithmetic_suite.addTest(TestArithmeticOperations("test_add"))
    arithmetic_suite.addTest(TestArithmeticOperations("test_sub"))
    arithmetic_suite.addTest(TestArithmeticOperations("test_mul"))
    arithmetic_suite.addTest(TestArithmeticOperations("test_div"))

    # arithmetic_tests = [
    #     TestArithmeticOperations("test_add"),
    #     TestArithmeticOperations("test_sub"),
    #     TestArithmeticOperations("test_mul"),
    #     TestArithmeticOperations("test_div"),
    # ]

    return arithmetic_suite


def make_statistical_suite():
    statistical_tests = [
        TestStatisticalOperations("test_mean"),
        TestStatisticalOperations("test_median_unsorted"),
        TestStatisticalOperations("test_median_even"),
        TestStatisticalOperations("test_median_odd"),
        TestStatisticalOperations("test_mode_single"),
        TestStatisticalOperations("test_mode_multiple"),
    ]

    statistical_suite = unittest.TestSuite()
    statistical_suite.addTests(statistical_tests)
    return statistical_suite


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestArithmeticOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestStatisticalOperations))
    return suite


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("option", choices=["S", "A"])
    # args = parser.parse_args()
    # # print(args)

    # if args.option.upper() == "S":
    #     suite = make_statistical_suite()
    # else:
    #     suite = make_arithmetic_suite()

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    unittest.main(verbosity=2)
