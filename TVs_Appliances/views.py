from django.shortcuts import render
from Electronics.models import ElectronicsModel

# Create your views here.
 
def index(request):
    return render (request,'TvAppliances_home_page.html')

def Televisions(request):
    data = ElectronicsModel.objects.filter(category__iexact = 'tv')
    context = {"data":data}
    return render(request,"Televisions.html",context)

def Air_conditioners(request):
    data = ElectronicsModel.objects.filter(category__iexact = 'AC')
    context = {"data":data}
    return render(request,"Televisions.html",context)

def Refrigerators(request):
    data = ElectronicsModel.objects.filter(category__iexact = 'Refrigerators')
    context = {"data":data}
    return render(request,"Televisions.html",context)

def Washing_machine(request):
    data = ElectronicsModel.objects.filter(category__iexact = 'washingmachine')
    context = {"data":data}
    return render(request,"Televisions.html",context)
