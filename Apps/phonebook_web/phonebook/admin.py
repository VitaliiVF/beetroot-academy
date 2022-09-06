from django.contrib import admin

from .models import Contact

# Register your models here.

@admin.register(Contact)
class PhonebookAdmin(admin.ModelAdmin):
    search_fields = ("email", "full_name", "phone")
    
    list_display = ("pk", "email", "full_name", "phone")
    
    list_display_links = ("pk", "email", "full_name")
    ordering = ("name",)
    pass

    
    @admin.display(boolean=True)
    def has_adress(self, Contact):
        return Contact.adress is not None and len(Contact.adress.strip()) > 0