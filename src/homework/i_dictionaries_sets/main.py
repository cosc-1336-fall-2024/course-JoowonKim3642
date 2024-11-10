#main

from dictionary import add_inventory, remove_inventory_widget

def menu():
    print("Inventory Menu\n1-Add or Update Item\n2-Delete Item\n3-Exit")

def main():
    inventory = {}

    while True:
        menu()
        choice = input("Enter your selection: ")

        if choice == '1':
            widget = input("item name: ")
            quantity = int(input("quantity: "))
            add_inventory(inventory, widget, quantity)
            print(f"Inventory updated: {inventory}\n")
        
        elif choice == '2':
            widget = input("Enter item name you want to delete: ")
            remove_inventory_widget(inventory, widget)
            print(f"Inventory after deletion: {inventory}\n")
        
        elif choice == '3':
            print("Exit")
            break
        
        else:
            print("Invalid value")
main()