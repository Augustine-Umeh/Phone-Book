import json

# Load the contact details from contacts.json
with open('contacts.json', 'r') as json_file:
    contacts_data = json.load(json_file)

# Sort the contact details based on Full name
sorted_contacts = dict(sorted(contacts_data.items(), key=lambda x: x[1]["full name"].lower()))

# Dump the sorted contacts into sorted_contacts.json
with open('sorted_contacts.json', 'w') as sorted_json_file:
    json.dump(sorted_contacts, sorted_json_file, indent=4)

print("Contact details sorted and saved to sorted_contacts.json.")
