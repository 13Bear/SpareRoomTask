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
            raise ValueError(f"Invalid data format for product '{code}' in productDataset. Expected a tuple of length 3.")
        price, specialQuantity, specialPrice = info
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError(f"Invalid price value '{price}' for product '{code}' in productDataset. Price must be a positive integer.")
        if specialQuantity is not None:
            if not isinstance(specialQuantity, int) or specialQuantity <= 0:
                raise ValueError(f"Invalid special quantity value '{specialQuantity}' for product '{code}' in productDataset. Quantity must be a positive integer or None.")
        if specialPrice is not None:
            if not isinstance(specialPrice, (int, float)) or specialPrice <= 0:
                raise ValueError(f"Invalid special price value '{specialPrice}' for product '{code}' in productDataset. Price must be a positive number or None.")

"""Retrieve and validate code and quantity from input list.
    Args:
        list: Input list

    Returns:
        formattedLidt: Formatted list so that it contains just Item Codes and their respective Quantities.
"""
def retrieveCodeAndQuantity(list):
    formattedList = []
    for item in list:
        code = item.get("code")
        quantity = item.get("quantity")
        
        try:
            validCodeCheck(code)
            validQuantityCheck(quantity)
            formattedList.append((code, quantity))
        except ValueError as e:
            print(f"Error: {e}")
    
    return formattedList

"""Calculate subtotal based on provided list.
    Args:
        list: Input list
    
    Returns:
        Formatted string containing subTotal, the price of all items.
"""
def checkout(list):
    try:
        validateProductDataset(productDataset)
        formattedList = retrieveCodeAndQuantity(list)
    except ValueError as e:
        return f"Error: {e}"

    subTotal = 0
    for item in formattedList:
        code = item[0]
        quantity = item[1]
        
        # Retrieve the price information from productDataset
        priceInfo = productDataset.get(code)
        if priceInfo:
            unitPrice = priceInfo[0]
            specialQuantity = priceInfo[1]
            specialPrice = priceInfo[2]
            
            # Calculate subtotal based on the quantity and pricing
            if specialQuantity and specialPrice:  # Check if special price is applicable
                subTotal += (quantity // specialQuantity) * specialPrice + (quantity % specialQuantity) * unitPrice
            else:
                subTotal += quantity * unitPrice
        else:
            return f"Error: {code} not found in productDataset"

    return f"Your subtotal is {subTotal}."