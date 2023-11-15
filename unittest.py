import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, 7)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
