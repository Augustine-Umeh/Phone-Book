import json

class DisplayAll:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path

    def display_all_contacts(self):
        count = 0
        print('\nThese are all the saved contacts\n')

        try:
            with open(self.file_path, 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No contacts found.")
            return

        for value in data.values():
            print(f"Name: {value.get('Full name', 'N/A')}")
            print(f"Phone number: {value.get('Phone number', 'N/A')}")
            if "address" in value:
                address = value['address']
                address_str = ", ".join(address.values())
                print(f"Address: {address_str}")
            print(f"Email: {value.get('Email Address', 'N/A')}")
            count += 1
            print("\n")

        print(f"There are {count} contacts.")
