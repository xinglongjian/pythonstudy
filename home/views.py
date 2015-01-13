from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from webcrawler.models import City,Weather
# Create your views here.

def index(request):
    citys=City.objects.all()
    return render(request,'home/index.html',{"menu":"home",'citys':citys})

def about(request):
    return render(request,'home/about.html',{"menu":"about"})

