from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# http://127.0.0.1:8000
def index(request):
    return HttpResponse("index")

def details(request):
    return HttpResponse("details")

def  list(request):
    return HttpResponse("list")

def  telefon(request):
    return HttpResponse("Telefon kategorisindeki ürünler")

def  bilgisayar(request):
    return HttpResponse("Bilgisayar kategorisindeki ürünler")


