from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from contact.models import ContactMe

class ContactForm(ModelForm):
    class Meta:
        model = ContactMe
        fields = ['email', 'subject', 'body']

def contact(request):
    if request.method == 'POST':
        email_info = ContactForm(request.POST)
        if email_info.is_valid():
            email_info.save()
    return render(request, 'contact.html', {

    })