def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter what you want to add: ")
            shopping_list.append(add_item)
            print(f"{add_item} was added to the list")
            pass
        elif choice == '2':
            remove_item = input("Select item to remove: ")
            # Prompt for and remove an item
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} was removed from the list")
            else:
                print(f"{remove_item} not found in list")
                pass
        elif choice == '3':
            for i in shopping_list:
                print(i) 
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")