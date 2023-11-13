# Initialize an empty inventory as a list of dictionaries
inventory = []

 # Function to add a new item to the inventory
def add_item():
     name = input("Enter item name: ")
     quantity = int(input("Enter quantity: "))
     price = float(input("Enter price: "))  # Corrected: Added closing parenthesis
     item = {"name": name, "quantity": quantity, "price": price}
     inventory.append(item)
     print(f"{name} has been added to the inventory.")

 # Function to update an existing item's quantity
def update_quantity():
     name = input("Enter the item name to update: ")
     quantity_change = int(input("Enter the quantity change (positive for addition, negative for removal): "))
     for item in inventory:
         if item["name"] == name:
             item["quantity"] += quantity_change
             print(f"Updated {name} quantity to {item['quantity']}.")
             return
     print(f"{name} not found in the inventory.")

 # Function to view the current inventory
def view_inventory():
     if not inventory:
         print("Inventory is empty.")
     else:
         print("Current Inventory:")
         for item in inventory:
             print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

 # Function to remove an item from the inventory
def remove_item():
     name = input("Enter the item name to remove: ")
     for item in inventory:
         if item["name"] == name:
             inventory.remove(item)
             print(f"{name} has been removed from the inventory.")
             return
     print(f"{name} not found in the inventory.")

 # Main loop to display the menu and handle user input
while True:
     print("\nMenu:")
     print("1. Add Item")
     print("2. Update Quantity")
     print("3. View Inventory")
     print("4. Remove Item")
     print("5. Exit")

     choice = input("Enter your choice: ")

     if choice == "1":
         add_item()
     elif choice == "2":
         update_quantity()
     elif choice == "3":
         view_inventory()
     elif choice == "4":
         remove_item()
     elif choice == "5":
         print("Exiting program.")
         break
     else:
         print("Invalid choice. Please choose a valid option.")