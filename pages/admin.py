from django.contrib import admin

from pages.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_ad']
    list_filter = ['created_ad']
    search_fields = ['name', 'email', 'message']

