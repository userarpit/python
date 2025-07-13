import unittest


class TestMembership(unittest.TestCase):
    def test_value_in_collection(self):
        a = 10
        b = [10, 20, 30]
        return self.assertIn(a, b)

    def test_value_not_in_collection(self):
        a = 10
        b = [20, 30, 40]
        return self.assertNotIn(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
