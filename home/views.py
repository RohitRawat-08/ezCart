from django.shortcuts import render,redirect
from Fashion.models import FashionModel
from Electronics.models import ElectronicsModel
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


def home(request):
    electronics_data = ElectronicsModel.objects.order_by('?')[:16]  
    fashion_data = FashionModel.objects.order_by('?')[:20]  
        
    context = {'f_data':fashion_data,'e_data':electronics_data }

    return render(request,'home.html',context)


def search(request):
    fashion_data={}
    electronics_data={}

    if request.method == "GET":
        if 'search' in request.GET:
            search = request.GET['search']

            fashion_data = FashionModel.objects.filter(Q(title__icontains=search) | Q(category__icontains=search))
            electronics_data = ElectronicsModel.objects.filter(Q(title__icontains=search) | Q(category__icontains=search))
        
        if fashion_data.count() == 0 and electronics_data.count() == 0 :
            context = {"nodata" : 'No Data Found'}
            return render(request , 'home.html' ,context)
            
    context = {"f_data":fashion_data, 'e_data':electronics_data}

    return render(request,'home.html',context)
