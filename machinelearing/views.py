from django.shortcuts import render

# Create your views here.
#-------------------Classification View-------------------------------------------
def classindex(request):
    return render(request,'machinelearing/classification/index.html',{"menu":"classification","submenu":"index"})
    
#-------------------Regression View-------------------------------------------    
def regreindex(request):
    return render(request,'machinelearing/regression/index.html',{"menu":"regression","submenu":"index"})

def singlevar(request):
    return render(request,'machinelearing/regression/singlevar.html',{"menu":"regression","submenu":"singlevar"})

def multivar(request):
    return render(request,'machinelearing/regression/multivar.html',{"menu":"regression","submenu":"multivar"})

def polynomial(request):
    return render(request,'machinelearing/regression/polynomial.html',{"menu":"regression","submenu":"polynomial"})

#-------------------Clustering View-------------------------------------------    
def clusterindex(request):
    return render(request,'machinelearing/clustering/index.html',{"menu":"clustering","submenu":"index"})