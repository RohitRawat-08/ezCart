from django.shortcuts import render
from Fashion.models import FashionModel
from Log_In.models import Address
# Create your views here.

def index(request):
    return render(request,'Fashion_home_page.html')

def Mens_Top_Wear(request):
    mens_top_wear = FashionModel.objects.filter(category__iexact = "Mentopwear")
    context ={"mtw":mens_top_wear }
    return render(request,"Mens_Top_Wear.html",context)

def Mens_Bottom_Wear(request):
    mens_bottom_wear = FashionModel.objects.filter(category__iexact = "MenBottomWear")
    context ={"mbw":mens_bottom_wear }
    return render(request,"Mens_Bottom_Wear.html",context)

def Men_Footwear(request):
    mens_foot_wear = FashionModel.objects.filter(category__iexact = "MenFootWear")
    context ={"mfw":mens_foot_wear }
    return render(request,"Men_Footwear.html",context)

def Women_Ethnic(request):
    women_ethnic_wear = FashionModel.objects.filter(category__iexact = "WomenEthnicWear")
    context ={"wew":women_ethnic_wear }
    return render(request,"Women_Ethnic.html",context)

def Women_Footwear(request):
    women_foot_wear = FashionModel.objects.filter(category__iexact = "WomenFootWear")
    context ={"wfw":women_foot_wear }
    return render(request,"Women_Footwear.html",context)

def kids(request):
    kids_wear = FashionModel.objects.filter(category__iexact = "kids")
    context ={"kw":kids_wear }
    return render(request,"kids.html",context)



def display_details(request ,id):
    data = FashionModel.objects.get(id=id)

    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user).first()
    else:
        address = "Login required"

    context ={'specific_item':data,"model_name":FashionModel._meta.model_name,"address":address}

    return render (request, "fashion_product_detail.html",context)