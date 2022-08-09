import re

class Email:
    
    def __init__(self, email):
        type(self).validate(email)
        self.email = email
    
    @classmethod    
    def validate(cls, email):
        prefix, domain = email.split("@")
        try:
            domain1, domain2 = domain.split(".")
        except ValueError:
            return print("Email is invalid")
            
        
        if not re.match(r"(^[a-zA-Z0-9_.+-]+$)", prefix):
            print("Email is invalid")
        elif prefix[0] in [".", "_", "+", "-"] or prefix[len(prefix)-1] in [".", "_", "+", "-"]:
            print("Email is invalid")
        elif prefix[prefix.find(".")] == prefix[prefix.find(".") + 1] and prefix.find(".") != -1:
            print("Email is invalid")
        elif prefix[prefix.find("_")] == prefix[prefix.find("_") + 1] and prefix.find("_") != -1:
            print("Email is invalid")
        elif prefix[prefix.find("-")] == prefix[prefix.find("-") + 1] and prefix.find("-") != -1:
            print("Email is invalid")
        elif not re.match(r"(^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", domain):
            print("Email is invalid")
        elif domain[domain.find(".")] == domain[domain.find(".") + 1] and domain.find(".") != -1:
            print("Email is invalid")
        elif domain[domain.find("_")] == domain[domain.find("_") + 1] and domain.find("_") != -1:
            print("Email is invalid111")
        elif domain[domain.find("-")] == domain[domain.find("-") + 1] and domain.find("-") != -1:
            print("Email is invalid111")
        elif len(domain2) < 2:
            print("Email is invalid")
        else:
            print("Email is valid")
        
# Prefix check
        
email1 = Email("abc-@mail.com") # invalid
email2 = Email("abc..def@mail.com") # invalid
email3 = Email(".abc@mail.com") # invalid
email4 = Email("abc#def@mail.com") # invalid
email5 = Email("abc-d@mail.com") # valid
email6 = Email("abc.def@mail.com") # valid
email7 = Email("abc@mail.com") # valid
email8 = Email("abc_def@mail.com") # valid

# Domains check

email11 = Email("abc.def@mail.c") # invalid
email12 = Email("abc.def@mail#archive.com") # invalid
email13 = Email("abc.def@mail") # invalid
email14 = Email("abc.def@mail..com") # invalid
email15 = Email("abc.def@mail.cc") # valid
email16 = Email("abc.def@mail-archive.com") # valid
email17 = Email("abc.def@mail.org") # valid
email18 = Email("abc.def@mail.com") # valid