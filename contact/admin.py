from django.contrib import admin
from contact.models import ContactMe

class ContactAdmin(admin.ModelAdmin):
    fields = ['email', 'subject', 'body']
    list_display = ('id', 'email', 'subject', 'body', 'created')

admin.site.register(ContactMe, ContactAdmin)
