import os
import json

class ClearAll:
    def __init__(self, file_path="contacts.json", id_path="name_id.json"):
        self.file_path = file_path
        self.id_path = id_path

    def clear_all_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "w") as json_file:
                json.dump({}, json_file)
            print("\nAll Contact details have been deleted. You no longer have any contacts.")
        else:
            print("\nNo contacts to delete.")

    def clear_all_id(self):
        if os.path.exists(self.id_path):
            with open(self.id_path, "w") as json_out:
                json.dump({}, json_out)
        else:
            print("\nNo ID data to delete.")

