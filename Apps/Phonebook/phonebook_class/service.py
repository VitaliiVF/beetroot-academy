import json

from .models import Contact

class ContactServise:
    
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        
        self.read_phonebook()
    
    def __iter__(self):
        return iter(self.contacts)
    
    def get_contacts(self):
        return self.contacts
    
    def add_contact(self, first_name, last_name, phone_number, email, city, notes = None, id = None):
        
        contact = Contact(first_name, last_name, phone_number, email, city, notes, id)
        
        self.contacts.append(contact)
        
        self.write_phonebook()
    
        return contact
    
    def search_contact(self, value):
        if value is None or len(value) == 0:
            raise ValueError("Value can't be empty")

        value = value.lower()
        result = []

        for contact in self.contacts:
            contact_first_name = contact.first_name.lower()
            contact_last_name = contact.last_name.lower()
            contact_full_name = contact.full_name.lower()
            contact_phone = contact.phone_number.lower()
            contact_city = contact.city.lower()
            
            if contact_first_name.find(value) != -1 \
                or contact_last_name.find(value) != -1 \
                or contact_full_name.find(value) != -1 \
                or contact_phone.find(value) != -1 \
                or contact_city.find(value) != -1:
                    
                result.append(contact)
        
        return result
    
    def remove_contact_by_name(self, full_name):
        if full_name is None or len(full_name) == 0:
            raise ValueError("Full name can't be empty")
        
        for contact in self.contacts:
            if full_name.lower() == contact.full_name.lower():
                self.contacts.remove(contact)
                
                self.write_phonebook()
                
                return True
        return False
        
    def update_contact(self, full_name, update, new_value):
        if full_name is None or len(full_name) == 0:
            raise ValueError("Full name can't be empty")
        
        if update is None or len(update) == 0:
            raise ValueError("Value can't be empty")
        
        full_name = full_name.lower()
        
        for contact in self.contacts:
                if contact.full_name.lower() == full_name:
                    
                    if update == "first_name":
                        contact.first_name = new_value
                        contact.full_name = f"{contact.first_name} {contact.last_name}"
                    
                    elif update == "last_name":
                        contact.last_name = new_value
                        contact.full_name = f"{contact.first_name} {contact.last_name}"
                    
                    elif update == "phone_number":
                        contact.phone_number = new_value
                    
                    elif update == "email":
                        contact.email = new_value
                    
                    elif update == "city":
                        contact.city = new_value
                    
                    elif update == "notes":
                        contact.notes = new_value
                        
                    else:
                        print("Not found to replace")

                    self.write_phonebook()
                            
                    return True
        return False
    
    
    def read_phonebook(self):
        with open(self.filename) as f:
            self.contacts = [
                Contact(c["first_name"], c["last_name"], c["phone_number"], c["email"], c["city"], c["notes"], c["id"]) for c in json.load(f)
            ]
            
    def write_phonebook(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)