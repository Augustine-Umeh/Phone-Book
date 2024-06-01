import json
import os

class AddContact:
    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path
        self.contacts = {}

    def add_contact(self):
        name = input("Enter full name (at least 3 characters): ").strip().lower()
        while len(name) < 3:
            print("Full name must have at least 3 characters.")
            name = input("Enter full name (at least 3 characters): ").strip().lower()

        number = input("Phone number: ").strip()
        while not number.isdigit() or len(number) < 10:
            print("Phone number must be at least 10 digits.")
            number = input("Phone number: ").strip()

        details = {}
        more_details = input("Do you want to add more details? (y/n): ").strip().lower()

        while more_details == 'y':
            details["street"] = input("Street: ").strip()
            details["city"] = input("City: ").strip()
            details["province"] = input("Province/State: ").strip()
            details["zip code"] = input("Zip code: ").strip()

            try:
                day, month, year = map(int, input("Enter your date of birth (DD MM YYYY): ").split())
                age = 2024 - year
            except ValueError:
                print("Invalid date format.")
                continue

            email = input("Email Address: ").strip()
            while '@' not in email or '.' not in email:
                print("Invalid email format.")
                email = input("Email Address: ").strip()

            self.contacts[name] = {
                "full name": name,
                "phone number": number,
                "address": details,
                "date of birth": f"{month}-{day}-{year}",
                "age": age,
                "email address": email
            }
            more_details = input("Do you want to add more details? (y/n): ").strip().lower()

        self.save_contacts()

    def save_contacts(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as json_file:
                json.dump({}, json_file)

        with open(self.file_path, "r") as json_file:
            try:
                existing_contacts = json.load(json_file)
            except json.JSONDecodeError:
                existing_contacts = {}

        existing_contacts.update(self.contacts)

        with open(self.file_path, "w") as json_file_out:
            json.dump(existing_contacts, json_file_out, indent=4)

    def convert_to_json(self):
        with open(self.file_path, "w") as json_file:
            json.dump(self.contacts, json_file, indent=4)

