from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Fashion.models import FashionModel
from Cart.models import Cart_Items
from Log_In.models import Address
from Electronics.models import ElectronicsModel

# Create your views here.
def index(request):
    try:
        if Cart_Items.objects.filter(user=request.user).count() != 0:
            cart_items = Cart_Items.objects.filter(user=request.user).order_by('-created_at')
            count = cart_items.count()
            item_amount=0
            for i in cart_items:
                item_amount += (i.price*i.quantity)
            price_details = {
                "item_amount": item_amount,
                "discount": 0,  
                "Platform_fees": 4,
                "delivery_charges": 30,
                "count": count,
            }
            total_amount = item_amount + price_details["discount"] + price_details["Platform_fees"] + price_details["delivery_charges"]

            address = Address.objects.filter(user=request.user).first()

            context = {
                "cart_items": cart_items,
                "price_details": price_details,
                "total_amount": total_amount,
                "address":address
            }
            return render(request, "cart_home_page.html", context)
        else:
            context={"msg":"no data found"}
            return render(request, "cart_home_page2.html", context)    
    except:
        return render(request, "cart_home_page.html")

@login_required(login_url='login')
def add_cart(request,model_name,id):

    if model_name == FashionModel._meta.model_name:
        data = FashionModel.objects.get(id=id)
        if Cart_Items.objects.filter(title=data.title, user=request.user).exists():
            item = Cart_Items.objects.get(title=data.title , user= request.user)
            item.quantity+=1
            item.save()

        else:
            cart_data = Cart_Items.objects.create(title=data.title,image_url=data.image_url,price=data.price,user=request.user)
            cart_data.save()

    elif model_name == ElectronicsModel._meta.model_name:
        data = ElectronicsModel.objects.get(id=id)
        if Cart_Items.objects.filter(title=data.title, user=request.user).exists():
            item = Cart_Items.objects.get(title=data.title , user= request.user)
            item.quantity+=1
            item.save()

        else:
            cart_data = Cart_Items.objects.create(title=data.title,image_url=data.image_url,price=data.price,user=request.user)
            cart_data.save()
    
    return redirect('cart')



def buy(request ,model_name,id):
    data={}
    total_amount = 0

    if model_name == FashionModel._meta.model_name:
        data = FashionModel.objects.get(id=id)
        price_details = {
                "item_amount": data.price,
                "discount": 0,  
                "Platform_fees": 4,
                "delivery_charges": 30,
                "count": 1,
                "quantity":1,
            }
        total_amount = data.price + price_details["discount"] + price_details["Platform_fees"] + price_details["delivery_charges"]
        model_name = FashionModel._meta.object_name

    if model_name == ElectronicsModel._meta.model_name:
        data = ElectronicsModel.objects.get(id=id)
        price_details = {
                "item_amount": data.price,
                "discount": 0,  
                "Platform_fees": 4,
                "delivery_charges": 30,
                "count": 1,
                "quantity":1,
            }
        total_amount = data.price + price_details["discount"] + price_details["Platform_fees"] + price_details["delivery_charges"]
        model_name = ElectronicsModel._meta.object_name


    address = Address.objects.filter(user=request.user).first()
    
    context={"data":data,
            "price_details":price_details,
            "total_amount":total_amount,
            "address":address,
            "model_name":model_name,
        }
    return render(request , "buyItems.html",context)






@login_required(login_url='login')
def remove_cart_itm(request,id):
    
    remove_itm = Cart_Items.objects.get(id=id)
    remove_itm.delete()

    return redirect('cart')