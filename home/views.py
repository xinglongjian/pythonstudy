from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home/index.html',{"menu":"home"})
    
def about(request):
    return render(request,'home/about.html',{"menu":"about"})

