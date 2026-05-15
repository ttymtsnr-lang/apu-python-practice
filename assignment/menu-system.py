# Toshinori Tsuchiyama
# TP064542

menu = {
    "coffee": {"price": 5.0, "stock": 3},
    "tea": {"price": 3.0, "stock": 5},
    "cake": {"price": 4.5, "stock": 2}
}

# Display menu
def display_menu():
    print("\n--- MENU ---")
    for item, details in menu.items():
        #menu.items() returns all menu items as pairs of item names and their details such as price and stock.
        #item represents the name of the menu item, while details represents the information of that item, such as price and stock.
        #the f".." is formatted string, {details['price]} is get price and RM is currency when its run itself.
        print(f"{item} - RM{details['price']} (Stock: {details['stock']})")


def search_item(name):
    if name in menu:
        print(f"{name} found. Price: RM{menu[name]['price']}, Stock: {menu[name]['stock']}")
    else:
        print("Item not found.")

# Place order
def place_order(name):
    if name not in menu:
        print("Item does not exist.")

    elif menu[name]["stock"] == 0:
        print("Item is sold out.")

    else:
        menu[name]["stock"] -= 1
        print(f"Order placed for {name}")
#This function is used to place an order for a menu item.
#First, it checks whether the item exists in the menu.
#Socondly, if the item does not exist, it shows an error message.
#Also, if the item exists but the stock is zero, it informs the user that the item is sold out.
#Otherwise, it reduces the stock by one and confirms that the order has been placed.

# Complete order
def complete_order(name):
    if name not in menu:
        print("Item does not exist.")

    elif menu[name]["stock"] == 0:
        print("The item is sold out.")

    else:
        print(f"Order for {name} completed.")
#It's almost the same function as the above "Place order" part.
#Except the reduce the number function(menu[name]["stock"] -= 1)

# Main loop
while True:
    print("\n1. Display Menu")
    print("2. Search Item")
    print("3. Place Order")
    print("4. Complete Order")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_menu()
    elif choice == "2":
        item = input("Enter item name: ").lower()
        search_item(item)
    elif choice == "3":
        item = input("Enter item name: ").lower()
        place_order(item)
    elif choice == "4":
        item = input("Enter item name: ").lower()
        complete_order(item)
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
