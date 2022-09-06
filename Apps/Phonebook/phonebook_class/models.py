import uuid

class Contact:
    
    def __init__(self, first_name, last_name, phone_number, email, city, notes = None, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.phone_number = phone_number
        self.email = email
        self.city = city
        self.notes = notes if notes is None else notes
        self.id = str(uuid.uuid4()) if id is None else id
                
    def __str__(self):
        return self.full_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return  self.last_name
    
    def get_full_name(self):
        return  self.full_name
    
    def get_phone_number(self):
        return  self.phone_number
    
    def get_email(self):
        return  self.email
    
    def get_city(self):
        return  self.city or "-"
    
    def get_notes(self):
        return  self.notes or "-"
    
    def get_id(self):
        return  self.id or "-"
    
    def to_dict(self):
        return self.__dict__