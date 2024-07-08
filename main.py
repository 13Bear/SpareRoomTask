productDataset = {
            "A": (50, 3, 140),
            "B": (35, 2, 60),
            "C": (25, None, None),
            "D": (12, None, None)
        }

def checkout(list):
    subTotal = 0
    formattedList = [(item["code"], item["quantity"]) for item in list] # reformats to give item code and quantity for each entry
    for item in formattedList:
        code = item[0]  # item[0] gives the item code ("A", "B", etc.)
        quantity = item[1]  # item[1] gives the quantity of the item
        
        # Retrieve the price information from productDataset
        priceInfo = productDataset.get(code)
        if priceInfo:
            unitPrice = priceInfo[0]  # First element in the tuple is price per
            if priceInfo[1] != None and priceInfo[2] != None: # provided elements have special prices
                specialQuantity = priceInfo[1] # Second element is quantity for the special price
                specialPrice = priceInfo[2] # Third element is special price
            
            # Calculate subtotal based on the quantity and pricing
            if priceInfo[1] != None and priceInfo[2] != None:  # Check if special price is applicable
                # first part of below calc multiplies the special price to the modulus of special quantities within total quantity requested
                # second part multiplies the remaining quantity after using speicial qunatity with the unit price
                # added to subTotal
                subTotal += (quantity // specialQuantity) * specialPrice + (quantity % specialQuantity) * unitPrice
            else:
                subTotal += quantity * unitPrice # added to subTotal
        else:
            print(f"Error: {code} not found in productDataset")
    
    return f"Your subtotal is {subTotal}."

exampleList = [{"code":"A","quantity":3},{"code":"B","quantity":3},{"code":"C","quantity":1},{"code":"D","quantity":2}] # example list given in task 

# Print the output
print(checkout(exampleList))
