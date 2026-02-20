import unittest

from app import calculate

class TestApp(unittest.TestCase):
   
    def test_addition(self):
        """Test addition operation"""
        result = calculate("1234567890 + 987654321")
        self.assertEqual(result, 1234567890+987654321)
    
    def test_subtraction(self):
        """Test subtraction operation"""
        result = calculate("1234567890 - 987654321")
        self.assertEqual(result, 1234567890 -987654321)
    
    def test_multiplication(self):
        """Test multiplication"""
        result = calculate("1234567890 * 987654321")
        self.assertEqual(result, 1234567890.0 * 987654321.0)
    
    def test_division(self):
        """Test division operation"""
        result = calculate("1234567890 / 987654321")
        self.assertEqual(result, 1234567890//987654321)
    
    def test_division_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ZeroDivisionError):
            calculate("10 / 0")


if __name__ == '__main__':
    unittest.main()