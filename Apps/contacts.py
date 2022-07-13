from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

print("Welcome to the Contacts v1.0!")

# Contact should contain name, email, phone, address (optional) and notes (optional)
contacts = [
    ('Janice Thomas', 'janice.thomas@example.com', '(272) 569-4415', '2745 Thornridge Cir', None),
    ('Cassandra Burton', 'cassandra.burton@example.com', '(629) 326-8652', None, None),
]

while True:
    print("""
a - add a contact
p - print list of contacts
d - delete a contact
q - quit from app
    """)

    action = Prompt.ask("Choise your action")

    if action == "q":
        print("Thank you! See you soon!")
        break
    elif action == "a":
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        phone = input("Enter a phone: ")
        address = input("Enter an address (optional): ")
        notes = input("Enter the notes (optional): ")

        address = address if len(address) > 0 else None
        notes = notes if len(notes) > 0 else None

        contact = (name, email, phone, address, notes)

        contacts.append(contact)
        print("Contact added successfully!")
    elif action == "p":
        table = Table(title="Contacts")

        table.add_column("Name", style="cyan")
        table.add_column("Email", style="cyan")
        table.add_column("Phone", style="magenta")
        table.add_column("Address")
        table.add_column("Notes")

        i = 0
        while i < len(contacts):
            contact = contacts[i]

            table.add_row(
                contact[0],
                contact[1],
                contact[2],
                contact[3] or "-",
                contact[4] or "-",
            )
            i += 1

        console = Console()
        console.print(table)
    elif action == "d":
        del_contact = input("Enter name of contact that you want delete or 'cancel': ")
        if del_contact == "cancel":
            continue
        else:
            for contact in contacts:
                if del_contact in contact:
                    contacts.remove(contact)
    else:
        print("Unknown action!")