from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'visualization/index.html',{"menu":"visualization","submenu":"index"})

def books(request):
    return render(request,'visualization/books.html',{"menu":"visualization","submenu":"books"})
    
def linechart(request):
    return render(request,'visualization/linechart.html',{"menu":"visualization","submenu":"linechart"})
    
def histogram(request):
    return render(request,'visualization/histogram.html',{"menu":"visualization","submenu":"histogram"})

def barchart(request):
    return render(request,'visualization/barchart.html',{"menu":"visualization","submenu":"barchart"})