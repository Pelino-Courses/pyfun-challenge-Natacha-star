
    #answers for number 4
class Product:
    """
    Represents a product in the inventory.

    Attributes:
        name (str): The name of the product.
        price (float): The price per unit.
        quantity (int): The quantity in stock.

    Methods:
        add_inventory(amount): Adds units to the inventory.
        remove_inventory(amount): Removes units from the inventory.
        total_value(): Returns the total value (price × quantity).
        display_info(): Prints product details.
    """

    def __init__(self, name, price, quantity):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, amount):
        if amount < 0:
            raise ValueError("Cannot add a negative amount.")
        self.quantity += amount

    def remove_inventory(self, amount):
        if amount < 0:
            raise ValueError("Cannot remove a negative amount.")
        if amount > self.quantity:
            raise ValueError("Not enough inventory to remove that amount.")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price per unit: ${self.price:.2f}")
        print(f"Quantity in stock: {self.quantity}")
        print(f"Total value: ${self.total_value():.2f}")


if __name__ == "__main__":
    
    print("Welcome to the Inventory Management System!")

    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("Error: Price must be a number, quantity must be an integer.")
        exit()

    try:
        product = Product(name, price, quantity)
        product.display_info()

        # Add inventory
        add_amount = int(input("How many units to add? "))
        product.add_inventory(add_amount)
        print("Inventory updated.")

        # Remove inventory
        remove_amount = int(input("How many units to remove? "))
        product.remove_inventory(remove_amount)
        print("Inventory updated.")

        # Final state
        print("\nFinal Product Info:")
        product.display_info()

    except ValueError as e:
        print(f"Error: {e}")

