# views.py
from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'home.html')

def helloworld(request):
    return render(request, "helloworld.html")