from django.shortcuts import render

# Create your views here.

#baseChart-----------------------------------------------------------------------------
def index(request):
    return render(request,'visualization/basechart/index.html',{"menu":"basechart","submenu":"index"})

def books(request):
    return render(request,'visualization/basechart/books.html',{"menu":"basechart","submenu":"books"})
    
def linechart(request):
    return render(request,'visualization/basechart/linechart.html',{"menu":"basechart","submenu":"linechart"})
    
def histogram(request):
    return render(request,'visualization/basechart/histogram.html',{"menu":"basechart","submenu":"histogram"})

def barchart(request):
    return render(request,'visualization/basechart/barchart.html',{"menu":"basechart","submenu":"barchart"})

def piechart(request):
    return render(request,'visualization/basechart/piechart.html',{"menu":"basechart","submenu":"barchart"})

def bubblechart(request):
    return render(request,'visualization/basechart/bubblechart.html',{"menu":"basechart","submenu":"bubblechart"})
    
def radarchart(request):
    return render(request,'visualization/basechart/radarchart.html',{"menu":"basechart","submenu":"radarchart"})

def candlestickchart(request):
    return render(request,'visualization/basechart/candlestickchart.html',{"menu":"basechart","submenu":"candlestickchart"})

#D3-------------------------------------------------------------------------------------------------------------------

def d3index(request):
    return render(request,'visualization/d3/d3index.html',{"menu":"d3","submenu":"index"})
    
def api_core(request):
    return render(request,'visualization/d3/api_core.html',{"menu":"d3","submenu":"api","collmenu":"core"})

def api_svg(request):
    return render(request,'visualization/d3/api_svg.html',{"menu":"d3","submenu":"api","collmenu":"svg"})