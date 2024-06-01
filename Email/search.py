import json

def display_found_contacts(found_contacts):
    display_data = []
    for contact in found_contacts:
        contact_info = {
            "Full name": contact["full name"],
            "Phone number": contact.get("phone number", "N/A"),
            "Email Address": contact.get("email address", "N/A"),
            "Address": contact.get("address", "N/A"),
            "Date of birth": contact.get("date of birth", "N/A"),
            "Age": contact.get("age", "N/A"),
        }
        display_data.append(contact_info)
    return display_data

class Search:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path

    def search_contacts(self, search_name):
        search_name = search_name.lower()
        not_found_contact = "Contact not found."

        try:
            with open(self.file_path, 'r') as json_out:
                file_data = json.load(json_out)
        except (FileNotFoundError, json.JSONDecodeError):
            return not_found_contact

        found_contacts = []
        for key, details in file_data.items():
            mod_key = key.split("_")[0].lower()
            if search_name in mod_key:
                found_contacts.append(details)

        if not found_contacts:
            return not_found_contact

        return display_found_contacts(found_contacts)


