# Phone Book

The Phone Book System is a comprehensive contact management application that allows users to add, search, display, edit, and delete contacts. This system also provides functionalities to clear all contacts and sort them for better organization.

## Features

- **Add Contacts**: Add new contacts with detailed information.
- **Search Contacts**: Search for contacts by full name.
- **Display All Contacts**: Display all stored contacts.
- **Edit Contacts**: Edit existing contact details.
- **Delete Contacts**: Delete contacts by searching and selecting.
- **Clear All Contacts**: Remove all contacts from the system.
- **Sort Contacts**: Sort contacts by full name.

## Requirements

- Python 3.6 or higher
- `contacts.json` and `name_id.json` files in the project directory for storing contacts and IDs.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/phone-book.git
   cd phone-book
   ```

2. Ensure `contacts.json` and `name_id.json` are present in the project directory. If not, create them:

   ```sh
   echo "{}" > contacts.json
   echo "{}" > name_id.json
   ```


## Usage

Run the `main.py` file to start the Phone Book.

```sh
python3 main.py
```

You will be presented with a menu with the following options:

1. Add Contact
2. Search Contact
3. Display All Contacts
4. Edit Contact
5. Delete Contact
6. Clear All Contacts
7. Exit

Enter the corresponding number to perform the desired action.

### Adding Contacts

Follow the prompts to add a new contact. You can enter the full name, phone number, and additional details like address, date of birth, and email address.

### Searching Contacts

Enter the full name of the contact you wish to search for. The system will display the contact details if found.

### Displaying All Contacts

Choose this option to display all saved contacts in the system.

### Editing Contacts

Enter the full name of the contact you wish to edit. Modify the details as prompted.

### Deleting Contacts

Enter the full name of the contact you wish to delete. Select the contact from the search results to delete it.

### Clearing All Contacts

Choose this option to delete all contacts from the system.

## Project Structure

- `add_contact.py`: Handles adding new contacts.
- `clear_all.py`: Handles clearing all contacts and IDs.
- `sort_contact.py`: Sorts contacts by full name.
- `store.py`: Contains logic for generating unique IDs and adding contacts.
- `search.py`: Handles searching for contacts.
- `DeleteContact.py`: Handles deleting contacts.
- `display_all.py`: Displays all contacts.
- `edit.py`: Handles editing existing contacts.
- `main.py`: The main entry point for the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please open an issue in the repository or contact the project maintainer.

---

