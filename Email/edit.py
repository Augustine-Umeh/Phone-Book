import json
import os
import random

def generate_unique_id(username, existing_ids):
    while True:
        random_number = random.randint(10000, 99999)
        generated_id = f"{username}_{random_number}"
        if generated_id not in existing_ids:
            return generated_id

class EditContact:
    def __init__(self, file_path="contacts.json", id_path="name_id.json"):
        self.file_path = file_path
        self.id_path = id_path

    def edit_contact(self):
        search_name = input("Please enter the full name of the contact to edit: ").strip().lower()
        found_contact = self.search_contact(search_name)

        if found_contact == "Contact not found.":
            print(found_contact)
        else:
            self.modify_contact(found_contact, search_name)

    def search_contact(self, search_name):
        try:
            with open(self.file_path, 'r') as json_out:
                file_data = json.load(json_out)
        except (FileNotFoundError, json.JSONDecodeError):
            return "Contact not found."

        for key, details in file_data.items():
            mod_key = key.split("_")[0].lower()
            if search_name in mod_key:
                return details, key
        return "Contact not found."

    def modify_contact(self, contact_data, search_name):
        contact_details, contact_id = contact_data
        print(f"Found Contact:\n{contact_details}\n")

        field_to_change = input("Enter the field to change (e.g., Full name, Phone number, Email Address, address, Date of birth): ").strip().lower()
        new_value = input(f"Enter the new {field_to_change}: ").strip()

        if field_to_change == "address":
            street = input("Street: ").strip()
            city = input("City: ").strip()
            province = input("Province/State: ").strip()
            postal_code = input("Postal code: ").strip()
            contact_details[field_to_change] = {
                "street": street,
                "city": city,
                "province": province,
                "postal code": postal_code
            }
        else:
            contact_details[field_to_change] = new_value

        try:
            with open(self.file_path, 'r') as json_file:
                existing_contacts = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_contacts = {}

        if field_to_change == "full name":
            new_id = generate_unique_id(new_value, existing_contacts)
            existing_contacts[new_id] = existing_contacts.pop(contact_id)
        else:
            existing_contacts[contact_id] = contact_details

        with open(self.file_path, 'w') as json_file_out:
            json.dump(existing_contacts, json_file_out, indent=4)

        print("Contact updated successfully!")

