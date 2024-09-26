class Item:
    def __init__(self, price, weight):
        """Initialize the Item with price and weight."""
        self.price = price
        self.weight = weight

# Example of code using the class
i = Item(10, 20)

# Accessing the attributes
print("Price:", i.price)   # Output: Price: 10
print("Weight:", i.weight)  # Output: Weight: 20
