from add_contact import AddContact
from clear_all import ClearAll
from search import Search
from Display_all import DisplayAll
from edit import EditContact
from DeleteContact import DeleteContact

def display_menu():
    print("\nPhone Book System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Clear All Contacts")
    print("7. Exit")

def main():
    contact_path = "contacts.json"
    id_path = "name_id.json"

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add Contact
            add_contact_instance = AddContact(contact_path, id_path)
            add_contact_instance.add_contact()
        elif choice == '2':
            # Search Contact
            search_instance = Search(contact_path)
            search_name = input("Enter the full name to search: ")
            result = search_instance.search_contacts(search_name)
            if result == "Contact not found.":
                print("\n", result)
            else:
                print("\nFound Contact:\n")
                for contact_info in result:
                    for key, value in contact_info.items():
                        print(f"{key}: {value}")
                    print("\n")
        elif choice == '3':
            # Display All Contacts
            display_all_instance = DisplayAll(contact_path)
            display_all_instance.display_all_contacts()
        elif choice == '4':
            # Edit Contact
            edit_instance = EditContact(contact_path, id_path)
            edit_instance.edit_contact()
        elif choice == '5':
            # Delete Contact
            delete_contact_instance = DeleteContact(contact_path, id_path)
            delete_contact_instance.delete_contact()
        elif choice == '6':
            # Clear All Contacts
            clear_all_instance = ClearAll(contact_path, id_path)
            clear_all_instance.clear_all_contacts()
            clear_all_instance.clear_all_id()
        elif choice == '7':
            # Exit
            print("Exiting the Phone Book System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
