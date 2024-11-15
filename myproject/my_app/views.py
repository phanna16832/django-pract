from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return render(request=request, template_name= 'helloworld.html')

def home(request):
    return render(request = request, template_name= 'home.html')  # r