from rich.console import Console

from phonebook_class.service import ContactServise
from phonebook_class.formatters import get_console_table

print("Welcome to the Phonebook v1.1!")

menu = """
a - add a contact
s - search a contact
u - update a contact
r - remove a contact
p - print list of contacts
q - quit from app
    """
    
console = Console()
    
def process_action(contact_service, action):
    
    if action == "q":
        print("Thank you! See you soon!")
        exit(0)
    
    elif action == "a":
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        phone_number = input("Enter a phone: ")
        email = input("Enter an email: ")
        city = input("Enter a city: ")
        notes = input("Enter the notes (optional): ")
        
        contact_service.add_contact(first_name, last_name, phone_number, email, city, notes)
        
        print("Contact added successfully!")
        
    elif action == "s":
        value = input("Search: ")
        
        contacts = contact_service.search_contact(value)
        
        if len(contacts) == 0:
            print("Contact not found")
        else:
        
            table = get_console_table(contacts, title = "Search")
            
            console.print(table)
       
    elif action == "u":
        full_name = input("Enter the full name of the contact you want to edit: ")
        
        contacts = contact_service.search_contact(full_name)
        
        if len(contacts) == 0:
            print("Contact not found")
        else:
        
            table = get_console_table(contacts, title = "Search")
            
            console.print(table)
            
            update = input("What exactly needs to be changed in a contact (first_name, last_name, phone_number, email, city or notes): ").lower()
            
            new_value = input(f"Enter a new {update}: ")
            
            try:
                ok = contact_service.update_contact(full_name, update, new_value)  
                
                if ok:
                    print("Contact updated successfully!")
                else:
                    print(f"Unable to update contact attribute: {update}")
                    
            except ValueError:
                print("Can't updated contact")
                
    
    elif action == "p":
        table = get_console_table(contact_service)
        console.print(table)
        
    elif action == "r":
        name = input("Enter a full name of contact that you want to delete: ")
        
        try:
            ok = contact_service.remove_contact_by_name(name)
            
            if ok:
                print("Contact removed successfully!")
            else:
                print(f"No contact found with {name}")
        except ValueError as err:
            print("Can't remove contact:", str(err))
    
    else:
        print("Unknown action!")


def main():
    
    filename = "phonebook_class/data_phonebook.json"
    
    contact_service = ContactServise(filename)
    
    while True:
                
        print(menu)
        
        action = input("Choise your action: ")
        
        process_action(contact_service, action)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank you. See you soon!")