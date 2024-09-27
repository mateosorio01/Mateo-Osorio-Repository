#Mateo Osorio, Assignment 2 
#I corrected my original code, since it lacked choice validation.
def display_menu():
    while True:
        print("\n1. Purchase an item")
        print("2. Load a new item")
        print("3. Remove an item")
        print("4. Refill an item")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def main(): #main function
    
    vending_machine = VendingMachine()
    
    print("Welcome to the vending machine program!")
    
    while True:
        choice = display_menu()
        
        if choice == "1":  # #this function is for purchusing, however the user needs to load an item before purchesing, otherwise it will show empty.
            description = input("Enter the name of the item you want to purchase: ")
            vending_machine.purchase_item(description)
        
        elif choice == "2":  # loading fuction, I reccomend to use first.
            description = input("Enter item name: ")
            price = float(input("Enter price (0.00 - 2.50): "))
            quantity = int(input("Enter quantity (1-20): "))
            try:
                new_item = Item(description, price, quantity)
                vending_machine.add_item(new_item)
            except ValueError as e:
                print(e)
        
        elif choice == "3":  # Remove item
            description = input("Enter the name of the item to remove: ")
            vending_machine.remove_item(description)
        
        elif choice == "4":  # Refill item
            description = input("Enter the name of the item to refill: ")
            quantity = int(input("Enter the quantity to add (1-20): "))
            try:
                vending_machine.refill_item(description, quantity)
            except ValueError as e:
                print(e)
        
        elif choice == "5":  # Quit
            print("Goodbye!")
            break

class VendingMachine: #this is the added class of vending machine, for assignment 2 
    def __init__(self, items=None):
        if items is None:
            items = []
        self._items = items

    def get_items(self):
        return self._items

    def add_item(self, item):
        if len(self._items) >= 10:
            print("No room to add more items.")
        else:
            self._items.append(item)
            print(f"Added {item.get_description()} to the vending machine.")

    def purchase_item(self, description):
        for item in self._items:
            if item.get_description().lower() == description.lower():
                if item.get_quantity() > 0:
                    print(f"Dispensing {item.get_description()}. Price: ${item.get_price():.2f}")
                    item.set_quantity(item.get_quantity() - 1)
                    if item.get_quantity() == 0:
                        self._items.remove(item)
                    return
                else:
                    print("Item is out of stock.")
                    return
        print("Item not found.")

    def remove_item(self, description):
        for item in self._items:
            if item.get_description().lower() == description.lower():
                self._items.remove(item)
                print(f"Removed {item.get_description()}.")
                return
        print("Item not found.")

    def refill_item(self, description, quantity):
        for item in self._items:
            if item.get_description().lower() == description.lower():
                item.set_quantity(item.get_quantity() + quantity)
                print(f"Refilled {item.get_description()}. New quantity: {item.get_quantity()}")
                return
        print("Item not found.")

class Item:   #this is the added class of Items, for assignment 2 
    def __init__(self, description, price=1.00, quantity=10):
        self.set_description(description)
        self.set_price(price)
        self.set_quantity(quantity)

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_price(self):
        return self._price

    def set_price(self, price):
        if 0.00 < price < 2.50:
            self._price = price
        else:
            raise ValueError("Price must be between $0.01 and $2.50")

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if 1 <= quantity <= 20:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be between 1 and 20")

    def __str__(self):
        return f"Item: {self._description}\nPrice: ${self._price:.2f}"

if __name__ == "__main__": #calling my main function.
    main()
