from django.forms import ModelForm
from contact.models import ContactMe


class ContactForm(ModelForm):
    class Meta:
        model = ContactMe
        fields = ['email', 'subject', 'body']