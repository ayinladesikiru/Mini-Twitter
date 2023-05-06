from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def homepage(request):
    name = "Asa"
    return render(request, 'home.html', {"name": name})
