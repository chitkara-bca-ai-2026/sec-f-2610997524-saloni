
inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("===== INVENTORY CONTROL SYSTEM =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("--- Current Inventory ---")
        for i in range(len(inventory)):
            print(i+1,".", inventory[i])

    elif choice == 2:
        item = input("Enter item name to add: ")
        inventory.append(item)
        print(item, "added to inventory.")

    elif choice == 3:
        item = input("Enter item name to remove: ")

        if item in inventory:
            inventory.remove(item)
            print(item, "removed from inventory.")
        else:
            print("Item not found!")

    elif choice == 4:
        inventory.sort()
        print("Inventory sorted alphabetically.")
        print(inventory)

    elif choice == 5:
        print("Thank you for using Inventory System!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
