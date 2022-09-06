from phonebook_class.service import ContactServise

def test_basic(tmp_phonebook):
    contact_service = ContactServise(tmp_phonebook)
    
    assert len(contact_service.get_contacts()) == 1
    
def test_add_contact(tmp_phonebook):
    contact_service = ContactServise(tmp_phonebook)
    
    contact_service.add_contact("Ivan", "Ivanov", "33333", "vewb@vew.uu", "Lviv")
    
    contact_service = ContactServise(tmp_phonebook)
    
    assert len(contact_service.get_contacts()) == 2
    
def test_search_contact(tmp_phonebook):
    contact_service = ContactServise(tmp_phonebook)
        
    assert len(contact_service.search_contact("Vitalii")) == 1
    
    contact_service.add_contact("Vitalii", "Ivanov", "33333", "vewb@vew.uu", "Lviv")
    
    assert len(contact_service.search_contact("Vitalii")) == 2
    
def test_remove_contact(tmp_phonebook):
    contact_service = ContactServise(tmp_phonebook)
    
    contact_service.remove_contact_by_name("Vitalii Fedun")
    
    assert len(contact_service.get_contacts()) == 0
    
def test_update_contact(tmp_phonebook):
    contact_service = ContactServise(tmp_phonebook)
    
    person = contact_service.add_contact("Ivan", "Ivanov", "33333", "vewb@vew.uu", "Lviv")
    
    contact_service.update_contact("Ivan Ivanov", "first_name", "Max")
    
    assert person.get_full_name() == "Max Ivanov"
    
   