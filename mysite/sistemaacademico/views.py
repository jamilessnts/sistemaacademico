from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> Essa é a página inicial do website!!!</h1>")

# Create your views here.
