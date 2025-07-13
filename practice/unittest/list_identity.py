import unittest


class TestListIdentity(unittest.TestCase):
    def test_list_alias(self):
        a = ["python", "unittest"]
        b = a
        return self.assertIs(a, b)

    def test_list_objects(self):
        a = ["python", "unittest"]
        b = ["python", "unittest"]
        return self.assertIsNot(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
