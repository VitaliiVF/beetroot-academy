from statistics import mode
from django.db import models

# Create your models here.


class SexOptions(models.TextChoices):
    MAN = "man", "Man"
    WOMAN = "woman", "Woman"
    OTHER = "other", "Other"


class Contact(models.Model):
    sex = models.CharField(max_length=10, default=SexOptions.MAN, choices=SexOptions.choices)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    full_name = full_name = f"{first_name} {last_name}"
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=150)
    notes = models.TextField(blank=True, null=True, default=None)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.email
    
    def __repr__(self):
        return f"<Contact {self.pk}, {self.email}, {self.full_name}, f{self.phone}>"
    
    