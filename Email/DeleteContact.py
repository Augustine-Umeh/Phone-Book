import json

class DeleteContact:
    def __init__(self, file_path="contacts.json", id_path="name_id.json"):
        self.file_path = file_path
        self.id_path = id_path

    def delete_contact(self):
        search_name = input("Please enter the full name of the contact to delete: ").strip().lower()
        
        # Search for the contact first
        search_instance = Search(self.file_path)
        found_contacts = search_instance.search_contacts(search_name)
        
        if not found_contacts:
            print("Contact not found.")
            return
        
        print("Found Contact(s):\n")
        for idx, contact_info in enumerate(found_contacts):
            print(f"{idx + 1}.")
            for key, value in contact_info.items():
                print(f"{key}: {value}")
            print("\n")

        try:
            choice = int(input("Enter the number of the contact you want to delete: ")) - 1
            if choice < 0 or choice >= len(found_contacts):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        contact_to_delete = found_contacts[choice]
        self._remove_contact(contact_to_delete)
        print("Contact deleted successfully.")

    def _remove_contact(self, contact_to_delete):
        with open(self.file_path, 'r') as json_file:
            existing_contacts = json.load(json_file)

        with open(self.id_path, 'r') as id_file:
            existing_ids = json.load(id_file)

        # Find the key to delete
        contact_id_to_delete = None
        for contact_id, details in existing_contacts.items():
            if details["full name"] == contact_to_delete["Full name"]:
                contact_id_to_delete = contact_id
                break
        
        if contact_id_to_delete:
            del existing_contacts[contact_id_to_delete]
            del existing_ids[contact_to_delete["Full name"]]

        with open(self.file_path, 'w') as json_file_out:
            json.dump(existing_contacts, json_file_out, indent=4)
        
        with open(self.id_path, 'w') as id_file_out:
            json.dump(existing_ids, id_file_out, indent=4)

# Import the Search class from search.py
from search import Search
