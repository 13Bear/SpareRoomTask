import unittest
from main import checkout, retrieveCodeAndQuantity, validCodeCheck, validQuantityCheck, validateProductDataset

class TestValidCodeCheck(unittest.TestCase):
    def test_invalid_code_not_string(self):
        self.assertRaises(ValueError, validCodeCheck, 123)  # Invalid code (not a string)

    def test_invalid_code_special_characters(self):
        self.assertRaises(ValueError, validCodeCheck, "AB!")  # Invalid code (contains special characters)

    def test_invalid_code_not_in_productDataset(self):
        self.assertRaises(ValueError, validCodeCheck, "E")  # Code not in productDataset

    def test_valid_code(self):
        self.assertIsNone(validCodeCheck("A"))  # Valid code

class TestValidQuantityCheck(unittest.TestCase):
    def test_invalid_quantity_not_integer(self):
        self.assertRaises(TypeError, validQuantityCheck, "abc")  # Quantity is not an integer

    def test_invalid_quantity_negative(self):
        self.assertRaises(ValueError, validQuantityCheck, -1)  # Quantity is negative

    def test_valid_quantity(self):
        self.assertIsNone(validQuantityCheck(5))  # Valid quantity

class TestRetrieveCodeAndQuantity(unittest.TestCase):
    def test_retrieve_code_and_quantity(self):
        exampleList = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}, {"code": "C", "quantity": 1}, {"code": "D", "quantity": 2}]
        self.assertEqual(retrieveCodeAndQuantity(exampleList), [("A", 3), ("B", 3), ("C", 1), ("D", 2)])

class TestValidateProductDataset(unittest.TestCase):
    def test_invalid_productDataset_missing_element(self):
        invalid_productDataset_1 = {
            "A": (50, 3, 140),
            "B": (35, 2, 60),
            "C": (25, None),  # Missing one element
            "D": (12, None, None)
        }
        self.assertRaises(ValueError, validateProductDataset, invalid_productDataset_1)

    def test_invalid_productDataset_negative_special_price(self):
        invalid_productDataset_2 = {
            "A": (50, 3, 140),
            "B": (35, 2, 60),
            "C": (25, None, -10),  # Negative special price
            "D": (12, None, None)
        }
        self.assertRaises(ValueError, validateProductDataset, invalid_productDataset_2)
        
    def test_valid_productDataset(self):
        valid_productDataset = {
            "A": (50, 3, 140),
            "B": (35, 2, 60),
            "C": (25, None, None),
            "D": (12, None, None),
            "E": (7, 4, 20)
        }
        self.assertIsNone(validateProductDataset(valid_productDataset)) # Correct productDataset

class TestCheckout(unittest.TestCase):
    def test_checkout_empty_list(self):
        self.assertEqual(checkout([]), "Your subtotal is 0.")

    def test_checkout_nonexistent_product_codes(self):
        exampleList = [{"code": "E", "quantity": 1}]
        self.assertEqual(checkout(exampleList), "Your subtotal is 0.")  # No valid items, subtotal is 0

    def test_checkout_mixed_valid_invalid_entries(self):
        exampleList = [{"code": "A", "quantity": 3}, {"code": "E", "quantity": 1}, {"code": "B", "quantity": 2}]
        self.assertEqual(checkout(exampleList), "Your subtotal is 200.")  # Only valid entries are considered

    def test_checkout_correct_calculation(self):
        exampleList = [{"code": "A", "quantity": 6}, {"code": "B", "quantity": 4}, {"code": "C", "quantity": 1}]
        self.assertEqual(checkout(exampleList), "Your subtotal is 425.")  # Correct subtotal
        exampleList = [{"code": "A", "quantity": 1}, {"code": "B", "quantity": 1}, {"code": "C", "quantity": 1}, {"code": "D", "quantity": 1}]
        self.assertEqual(checkout(exampleList), "Your subtotal is 122.")

    def test_checkout_input_with_non_string_codes(self):
        exampleList = [{"code": 123, "quantity": 1}]
        self.assertEqual(checkout(exampleList), "Your subtotal is 0.")  # Invalid code is ignored, subtotal is 0

if __name__ == "__main__":
    unittest.main()
