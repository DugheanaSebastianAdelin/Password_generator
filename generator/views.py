from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
def password(request):
    thepassword=''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))


    lenght = int(request.GET.get('length',13))
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword })



def about(request):
    return render(request, 'generator/about.html')
