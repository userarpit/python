import unittest
from age import categorized_by_age
import sys


class TestCategorizeByAge(unittest.TestCase):
    @unittest.skip("no condition")
    def test_child(self):
        """Test that an age of 5 is correctly categorized as 'Child'."""

        self.assertEqual(categorized_by_age(5), "Child")

    def test_adolescent(self):
        """Test that an age of 15 is correctly categorized as 'Adolescent'."""
        self.assertEqual(categorized_by_age(15), "Adolescent")

    def test_adult(self):
        """Test that an age of 30 is correctly categorized as 'Adult'."""
        self.assertEqual(categorized_by_age(30), "Adult")

    def test_golden_age(self):
        """Test that an age of 70 is correctly categorized as 'Golden Age'."""
        self.assertEqual(categorized_by_age(70), "Golden Age")

    def test_negative_age(self):
        """Test that an age of -1 is correctly categorized as 'Invalid age: -1'."""
        self.assertEqual(categorized_by_age(-1), "Invalid age: -1")

    def test_too_old(self):
        """Test that an age of 151 is correctly categorized as 'Invalid age: 151'."""
        self.assertEqual(categorized_by_age(151), "Invalid age: 151")

    def test_boundary_child_adolescent(self):
        """Test that an age of 9 is correctly categorized as 'Child'
        and an age of 10 is correctly categorized as 'Adolescent'."""
        self.assertEqual(categorized_by_age(9), "Child")
        self.assertEqual(categorized_by_age(10), "Adolescent")

    def test_boundary_adolescent_adult(self):
        """Test that an age of 18 is correctly categorized as 'Adolescent'
        and an age of 19 is correctly categorized as 'Adult'."""

        self.assertEqual(categorized_by_age(18), "Adolescent")
        self.assertEqual(categorized_by_age(19), "Adult")

    def test_boundary_adult_golden_age(self):
        """Test that an age of 65 is correctly categorized as 'Adult'
        and an age of 66 is correctly categorized as 'Golden Age'."""
        self.assertEqual(categorized_by_age(65), "Adult")
        self.assertEqual(categorized_by_age(66), "Golden Age")

    @unittest.skip("Unconditionally skipped test")
    def test_unimportant(self):
        self.fail("The test should be skipped")

    @unittest.skipIf(sys.version_info < (3, 12), "Requires Python >= 3.12")
    def test_using_calendar_constants(self):
        import calendar

        self.assertEqual(calendar.Month(10), calendar.OCTOBER)

    @unittest.skipUnless(sys.platform.startswith("win"), "Requires Windows")
    def test_windows_support(self):
        from ctypes import WinDLL, windll

        self.assertIsInstance(windll.kernel32, WinDLL)


if __name__ == "__main__":
    unittest.main(verbosity=2)
