from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    content = {
        'password':'random generate password : xxx'
    }
    return render(request,'generator/home.html', content)

def password(request):
    characters = list('abcdefghijklmnoprstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    length = int(request.GET.get('length',12)) # second argument is the default value (password length) - optional
    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters)
    content = {
        'the_password': thepassword
    }
    return render(request,'generator/password_view.html', content)

def aboutme(request):
    return render(request, 'generator/aboutme.html')


