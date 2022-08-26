from rich.table import Table

from .models import Contact

def get_console_table(contacts, title = "Contacts"):
    
    table = Table(title=title)

    table.add_column("Name", style="magenta")
    table.add_column("Phone number", style="cyan")
    table.add_column("Email", style="magenta")
    table.add_column("City", style="cyan")
    table.add_column("Notes", style="magenta")
    
    if isinstance(contacts, Contact):
        contacts = [contacts]

    for contact in contacts:
        table.add_row(
            contact.get_full_name(),
            contact.get_phone_number(),
            contact.get_email(),
            contact.get_city(),
            contact.get_notes() or "-"
        )
    
    return table