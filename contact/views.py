from django.shortcuts import render
from contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        email_info = ContactForm(request.POST)
        if email_info.is_valid():
            email_info.save()
    return render(request, 'contact.html', {
    })
