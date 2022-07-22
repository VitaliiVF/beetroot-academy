import uuid
import json

from rich.console import Console
from rich.table import Table

filename = "data_phonebook.json"

with open(filename, "r") as f:
    contacts = json.load(f)

def remove_contact_by_name(name):
    if name is None or len(name) == 0:
        raise ValueError("Full name can't be empty")
    
    contacts = get_contacts()
    
    for contact in contacts:
        if name.lower() == contact["full name"].lower():
            contacts.remove(contact)
            return True
    return False            

def get_contacts():
    return contacts

def search_contact(value):
    if value is None or len(value) == 0:
        raise ValueError("Value can't be empty")

    value = value.lower()

    contacts = get_contacts()

    for contact in contacts:
        contact_first_name = contact["first name"].lower()
        contact_last_name = contact["last name"].lower()
        contact_full_name = contact["full name"].lower()
        contact_phone = contact["phone number"].lower()
        contact_city = contact["city"].lower()
        
        if contact_first_name.find(value) != -1 \
            or contact_last_name.find(value) != -1 \
            or contact_full_name.find(value) != -1 \
            or contact_phone.find(value) != -1 \
            or contact_city.find(value) != -1:
            return contact
    
    return False

def update_contact(full_name):
    if full_name is None or len(full_name) == 0:
        raise ValueError("Full name can't be empty")
    
    full_name = full_name.lower()
    
    contacts = get_contacts()    
    
    for contact in contacts:
            if contact["full name"].lower() == full_name:
                update = input("What exactly needs to be changed in a contact (first name, last name, phone number, email, city or notes): ").lower()
                for k in contact:
                    if update == k:
                        contact[k] = input(f"Enter a new {update}: ")
                        return contacts
    return False

print("Welcome to the Phonebook v1.0!")

while True:
    print("""
a - add a contact
s - search a contact
u - update a contact
r - remove a contact
p - print list of contacts
q - quit from app
    """)
    
    action = input("Choise your action: ")
    
    if action == "q":
        print("Thank you! See you soon!")
        break
    
    elif action == "a":
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        full_name = first_name + " " + last_name
        phone_number = input("Enter a phone: ")
        email = input("Enter an email: ")
        city = input("Enter a city: ")
        notes = input("Enter the notes (optional): ")
        
        notes = notes if len(notes) > 0 else None
        
        contact = {
            "id": str(uuid.uuid4()),
            "first name": first_name, 
            "last name": last_name,
            "full name": full_name,
            "phone number": phone_number,
            "email": email,  
            "city": city, 
            "notes": notes
        }

        contacts.append(contact)
        
        with open(filename, "w") as f:
            json.dump(contacts, f, indent=2)
            
        print("Contact added successfully!")
    
    elif action == "s":
        value = input("Enter the contact's name, phone number or city: ")
        
        try:
            contact = search_contact(value)
            
            if contact:
            
                table = Table(title="Search result")
                
                table.add_column("Name")
                table.add_column("Phone number")
                table.add_column("Email")
                table.add_column("City")
                table.add_column("Notes")
                
                table.add_row(
                        contact["full name"],
                        contact["phone number"],
                        contact["email"],
                        contact["city"],
                        contact["notes"] or "-"
                    )

                console = Console()
                console.print(table)
            else:
                print("Contact not found...")
        except ValueError as err:
            print("Can't search contact:", str(err))
            
    elif action == "u":
        full_name = input("Enter the full name of the contact you want to edit: ")
                
        try:            
            if update_contact(full_name):
                print("Contact successfully changed")
                
                with open(filename, "w") as f:
                    json.dump(contacts, f, indent=2)
            
                table = Table(title="Update result")
                
                table.add_column("Name")
                table.add_column("Phone number")
                table.add_column("Email")
                table.add_column("City")
                table.add_column("Notes")
                
                for contact in contacts:
                    if contact["full name"].lower() == full_name:
                        table.add_row(
                            contact["full name"],
                            contact["phone number"],
                            contact["email"],
                            contact["city"],
                            contact["notes"] or "-"
                        )

                console = Console()
                console.print(table)
            else:
                print("Contact not found...")
        except ValueError as err:
            print("Can't search contact:", str(err))
        
    elif action == "p":
        table = Table(title="Contacts")

        table.add_column("Name")
        table.add_column("Phone number")
        table.add_column("Email")
        table.add_column("City")
        table.add_column("Notes")

        for contact in contacts:
            table.add_row(
                contact["full name"],
                contact["phone number"],
                contact["email"],
                contact["city"],
                contact["notes"] or "-"
            )

        console = Console()
        console.print(table)
        pass
    
    elif action == "r":
    
        name = input(
            "Enter a full name of contact that you want to delete: ")
        
        try:
            if remove_contact_by_name(name):
                print("Contact removed successfully!")
                with open(filename, "w") as f:
                    json.dump(contacts, f, indent=2)
            else: print(f"No contact found with full name: {name}")
        except ValueError as err:
            print("Can't remove contact:", str(err))
            
    else:
        print("Unknown action!")