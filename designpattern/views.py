from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'designpattern/index.html',{"menu":"pattern","submenu":"index"})

#abstractfactory  
def abstractfactory(request):
    return render(request,'designpattern/abstractfactory.html',{"menu":"pattern","submenu":"abstractfactory"})