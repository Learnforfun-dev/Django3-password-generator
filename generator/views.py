from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    charaters=list('abcdefghijklmnopqrstuvwxyz')
    password=''
    length= request.GET.get('length', 10) ## added default length 10. this is optional
    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charaters.extend(list('!&^$@%#*?_-'))
    if request.GET.get('number'):
        charaters.extend(list('1234567890'))
    for x in range(int(length)):
        password = password+ random.choice(charaters)
  
    return render(request, 'generator/password.html', {'password':password})

def about(request):
    return render(request, 'generator/about.html')