from phonebook_class.models import Contact

first_name = "Vitalii"
last_name = "Fedun"
full_name = "Vitalii Fedun"
phone_number = "0988888888"
email = "defe@vreb.vv"
city = "Odesa"
notes = None


def test_auto_id():
    test_contact = Contact(first_name, last_name, full_name, phone_number, email, city, notes)
    
    assert test_contact.id is not None
    
def test_str():
    test_contact = Contact(first_name, last_name, full_name, phone_number, email, city, notes)
    
    assert str(test_contact) == test_contact.full_name
    
def test_feull_name():
    test_contact = Contact(first_name, last_name, full_name, phone_number, email, city, notes)
    
    assert test_contact.full_name == test_contact.first_name + " " + test_contact.last_name 
    
def test_to_dict():
    test_contact = Contact(first_name, last_name, full_name, phone_number, email, city, notes)
    
    data = test_contact.to_dict()
    
    assert type(data) == dict
    assert test_contact.get_first_name() == data["first_name"]
    assert test_contact.get_last_name() == data["last_name"]
    assert test_contact.get_full_name() == data["full_name"]
    assert test_contact.get_phone_number() == data["phone_number"]
    assert test_contact.get_email() == data["email"]
    assert test_contact.get_city() == data["city"]