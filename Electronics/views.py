from django.shortcuts import render
from Electronics.models import ElectronicsModel
from Log_In.models import Address

# Create your views here.

def index(request):
    return render(request ,"Electronics_home_page.html")

def Cameras_Accessories(request):
    data = ElectronicsModel.objects.filter(category__iexact ='Camera')
    context={"data":data}    
    return render(request , "CamerasLaptop.html",context)

def laptop_desktop(request):
    data = ElectronicsModel.objects.filter(category__iexact ='Laptop')
    context={"data":data}
    return render(request , "CamerasLaptop.html",context)

def HeadPhones(request):
    data = ElectronicsModel.objects.filter(category__iexact ='headphone')
    context={"data":data}
    return render(request , "HeadMobilePower.html",context)

def Mobile_Accessories(request):
    data = ElectronicsModel.objects.filter(category__iexact ='MobileAcc')
    context={"data":data}
    return render(request , "HeadMobilePower.html",context)

def Powerbank(request):
    data = ElectronicsModel.objects.filter(category__iexact ='powerbank')
    context={"data":data}
    return render(request , "HeadMobilePower.html",context)


def Electronic_Product_Details(request ,id):
    specific_item = ElectronicsModel.objects.get(id=id)

    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user).first()
    else:
        address = "Login required"
    context={"specific_item":specific_item,"address":address,"model_name":ElectronicsModel._meta.model_name}
    return render (request, "Electronic_Product_Details.html",context,)











