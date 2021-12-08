from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    n = list(string.ascii_lowercase)
    thepassword = ''
    if request.GET.get('uppercase'):
        n.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        n.extend(list(string.digits))
    if request.GET.get('sumbol'):
        n.extend(list('!@#$%&*+='))
    length = request.GET.get('length', 12)
    for i in range(int(length)):
        thepassword += random.choice(n)

    return render(request, 'generator/password.html', {'password': thepassword})


def info(request):
    return render(request, 'generator/info.html')
