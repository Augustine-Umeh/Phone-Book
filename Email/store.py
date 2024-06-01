import json
import random
import os

def generate_unique_id(username, existing_ids):
    while True:
        random_number = random.randint(10000, 99999)
        generated_id = f"{username}_{random_number}"
        if generated_id not in existing_ids:
            return generated_id

class AddContact:
    def __init__(self, contact_path="contacts.json", id_path="name_id.json"):
        self.file_path = contact_path
        self.id_path = id_path
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

        try:
            with open(self.id_path, "r") as id_file:
                existing_id_data = json.load(id_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_id_data = {}

        contact_id = generate_unique_id(name, existing_id_data)
        existing_id_data[name] = contact_id

        more_details = input("Do you want to add more details? (y/n): ").strip().lower()

        self.contacts[contact_id] = {
            "full name": name,
            "phone number": number,
        }

        details = {}
        while more_details == 'y':
            details["street"] = input("Street: ").strip()
            details["city"] = input("City: ").strip()
            details["province"] = input("Province/State: ").strip()
            details["postal code"] = input("Postal code: ").strip()

            try:
                day, month, year = map(int, input("Enter your date of birth (DD MM YYYY): ").split())
                age = 2023 - year
            except ValueError:
                print("Invalid date format.")
                continue

            email = input("Email Address: ").strip().lower()
            while '@' not in email or '.' not in email:
                print("Invalid email format.")
                email = input("Email Address: ").strip().lower()

            date_of_birth = f"{month}-{day}-{year}"

            self.contacts[contact_id] = {
                "full name": name,
                "phone number": number,
                "address": details,
                "date of birth": date_of_birth,
                "age": age,
                "email address": email,
            }
            break

        with open(self.id_path, "w") as id_file:
            json.dump(existing_id_data, id_file, indent=4)

        self.save_contact_json()

    def save_contact_json(self):
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

