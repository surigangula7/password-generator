from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generatorApp/home.html')

# def eggs(request):
#     return HttpResponse("<h1>Eggs are awesome</h1>")


def about(request):
    return render(request, 'generatorApp/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if  request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generatorApp/password.html', {'password': thepassword})
