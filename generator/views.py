import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*-+/')
    if request.GET.get('numbers'):
        characters.extend('0123456789')

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    text_on_the_page = '''Hello everyone. My name is madkisya. I am just starting to explore sites and am trying to find ways to realize my mind. Thank you very much 
    for viewing this page. See you! '''
    return render(request, 'generator/about.html', {'creator': text_on_the_page}) # creator - слово ссылки в файл html
