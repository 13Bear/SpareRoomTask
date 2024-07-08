productDataset = {
            "A": (50),
            "B": (30),
            "C": (20),
            "D": (15)
        }

def checkout(formattedList):
    subTotal = 0
    for item in desiredOutput:
        subTotal += productDataset.get(item[0])*item[1]
    return subTotal

exampleList = [{"code":"A","quantity":3},{"code":"B","quantity":3},{"code":"C","quantity":1},{"code":"D","quantity":2}]

desiredOutput = [(item["code"], item["quantity"]) for item in exampleList]

# Print the output
print(checkout(desiredOutput))
