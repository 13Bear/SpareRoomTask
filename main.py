productDataset = {
    "A": (50, 3, 140),
    "B": (35, 2, 60),
    "C": (25, None, None),
    "D": (12, None, None)
}

"""Check if code is alpha and exists in productDataset.
    Args:
    code: Item Code at that index

    Raises:
        ValueError: If code is not a single letter from a-z/A-Z.
"""
def validCodeCheck(code):
    if not isinstance(code, str) or not code.isalpha():
        raise ValueError(f"Invalid code: '{code}'. Code must be an aplha charcter.")
    if code not in productDataset:
        raise ValueError(f"Product with code '{code}' not found in productDataset.")

"""Check if quantity is a positive integer.
    Args:
        quantity: Quantity of Item Code requested.

    Raises:
        ValueError: If quantity is not greater than 0.
        TypeError: If quantity is not an integer.
"""
def validQuantityCheck(quantity):
    if not isinstance(quantity, int):
        raise TypeError(f"Invalid quantity: '{quantity}'. Quantity must be a positive integer value (not a string, Bool, Float, etc)")
    if quantity <= 0:
        raise ValueError(f"Invalid quantity: '{quantity}'. Quantity must be a positive integer.")

"""Validate the productDataset dictionary.
    Args:
        productDataSet: Dictionary containing Item Codes and their respective unit and special prices.
        code: Item Code at index.
        price: Unit Price at index.
        specialQuantity: Quantity required for special pricing at index.
        specialPrice: Special Price of Item at index.

    Raises:
        ValueError: If entry in dictionary is not a tuple of length 3.
        ValueError: If price is not a positive integer.
        ValueError: If specialQuantity is not a positive int or None
        ValueError: If specialPrice is not a positive int or None
"""
def validateProductDataset(productDataset):
    for code, info in productDataset.items():
        if not isinstance(info, tuple) or len(info) != 3:
            raise ValueError(f"Invalid data format for product '{code}