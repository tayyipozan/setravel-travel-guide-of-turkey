from django.shortcuts import render
from django.contrib import messages
from .models import Contact

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def mainpage(request):
    if 'email' in request.POST:
        contact(request)
    return render(request, 'pages/MainPage.html')

def contact(request):
        contactemail = request.POST['email'].strip()
        contactname= request.POST['name'].strip()
        contacttext = request.POST['text'].strip()
        Contact.objects.create(id='NULL', contactemail=contactemail, contactname=contactname, contacttext=contacttext )
        messages.add_message(request, messages.SUCCESS, 'Your message has been sent to us. We will send an e-mail as soon as possible.')