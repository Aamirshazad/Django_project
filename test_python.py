import unittest
from my_code import my_function

class TestMyFunction(unittest.TestCase):
    
    def test_my_function_with_valid_input(self):
        result = my_function(5)
        self.assertEqual(result, 25)
        
    def test_my_function_with_negative_input(self):
        result = my_function(-5)
        self.assertEqual(result, 0)
        
    def test_my_function_with_zero_input(self):
        result = my_function(0)
        self.assertEqual(result, 0)
        rt
if __name__ == '__main__':
    unittest.main()
