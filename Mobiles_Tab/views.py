from django.shortcuts import render
from django.db.models import Q
from Electronics.models import ElectronicsModel


# Create your views here.

def index(request):

    return render (request ,"mobile_tab_home_page.html")


# !Apple Products
def AppleProducts(request):
    AppleProduct = ElectronicsModel.objects.filter(brand__iexact='Apple' , category__iexact='mobile' )
    context = {"product":AppleProduct}
    return render (request ,"Apple.html",context)


# !Samsung Products
def SamsungProducts(request):
    SamsungProduct = ElectronicsModel.objects.filter(brand__iexact="Samsung", category__iexact='mobile')

    context = {"product":SamsungProduct}
    return render (request ,"Apple.html",context)

# !RealmeProducts
def RealmeProducts(request):
    RedmiProduct = ElectronicsModel.objects.filter(brand__iexact='redmi', category__iexact='mobile')

    context = {"product":RedmiProduct}
    return render (request ,"Apple.html",context)

# !PocoProducts
def PocoProducts(request):
    PocoProduct = ElectronicsModel.objects.filter(brand__iexact='poco', category__iexact='mobile')
    context = {"product":PocoProduct}
    return render (request ,"Apple.html",context)

# !OnePlusProducts
def OnePlusProducts(request):
    OnePlusProduct = ElectronicsModel.objects.filter(brand__iexact='oneplus', category__iexact='mobile')
    context = {"product":OnePlusProduct}
    return render (request ,"Apple.html",context)

# !show Product detail
# def Product_Details(request ,id):
#     Product = Mobile.objects.get(id=id)
#     if request.user.is_authenticated:
#         address = Address.objects.get(user=request.user)
#     else:
#         address = "Login required"
#     context = {'specific_item':Product,"model_name":Mobile._meta.model_name,"address":address}
#     return render (request, "Product_Details.html",context)






