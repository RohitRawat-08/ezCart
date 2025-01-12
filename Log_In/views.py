from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from Log_In.models import Address ,ProfileImage ,MyOrdersModel
from Fashion.models import FashionModel
from Electronics.models import ElectronicsModel
from Cart.models import Cart_Items
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.
@csrf_exempt
def index(request):
   
    if request.method == "POST":
        User_Name = request.POST['username']
        # User_Email = request.POST['email']
        User_Password = request.POST['password']
        
        user=authenticate(username=User_Name,password=User_Password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render( request ,'wrong.html')
    
    return render( request ,'LogIn_home_page.html')

def New_Registration(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        User_Name = request.POST['username']
        User_Email = request.POST['email']
        User_Password = request.POST['password']

        data = User.objects.create(first_name=f_name, last_name=l_name, username=User_Name,email=User_Email,password=User_Password)
        data.set_password(User_Password)
        data.save()

        return redirect("login")
    return render(request , 'New_Registration.html') 

def logout_(request):
    logout(request)
    return redirect('login')


login_required(login_url='login')
def profile(request):
    try:
        data = ProfileImage.objects.get(user = request.user)
        context={"data":data}

    except:
        context={}
    
    return render(request , "profile.html",context)






# login_required(login_url='login')
def add_profile_img(request):

    if ProfileImage.objects.filter(user=request.user).count() == 0:
        if request.method == 'POST':
            if 'image' in request.FILES:
                profile_image = request.FILES['image']
                user = request.user
                
                ProfileImage.objects.create(image=profile_image,user=user)

                return redirect('profile')  # Redirect to the profile page
            # else:
            #     print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
            #     return render(request, 'profile.html', {'error': 'No file was selected!'})
    else:
        data = ProfileImage.objects.get(user=request.user)
        if request.method == 'POST':
            profile_image = request.FILES['image']
            
            data.image = profile_image
            data.save()
            return redirect('profile')  # Redirect to the profile page



    return render(request , "add_profile_img.html")







login_required(login_url='login')
def my_order(request,model_name,id):
    # print(id)
    # print(model_name)

    order_id = str(random.randint(10**11, 10**12 - 1))
    
    if model_name == FashionModel._meta.object_name:
        data = FashionModel.objects.get(id=id)
        o_data = MyOrdersModel.objects.create(order_id = order_id,title=data.title,img_url=data.image_url,price=data.price,user=request.user)
        o_data.save()

    elif model_name == ElectronicsModel._meta.object_name:
        data = ElectronicsModel.objects.get(id=id)
        o_data = MyOrdersModel.objects.create(order_id = order_id,title=data.title,img_url=data.image_url,price=data.price,user=request.user)
        o_data.save()
        
    return redirect('my_orders_list')



def place_order_f_cart(request):
    data = Cart_Items.objects.all()


    for i in data:
        order_id = str(random.randint(10**11, 10**12 - 1))
        o_data = MyOrdersModel.objects.create(order_id = order_id,title=i.title,img_url=i.image_url,price=i.price*i.quantity,quantity= i.quantity, user=request.user)
        o_data.save()

    data.delete()


    return redirect('my_orders_list')




def my_order_list(request):
    data = MyOrdersModel.objects.filter(user=request.user).order_by('-created_at')
    context={"data":data}
    return render(request , "my_order.html",context)
    



login_required(login_url='login')
def profile_info(request):
    data = Address.objects.filter(user=request.user)
    context= {"data":data}
    return render(request , "profile_info.html",context)





login_required(login_url='login')
def manage_add(request):
    if request.method == "POST":
        name = request.POST['uname']
        number = request.POST['number']
        pincode = request.POST['pincode']
        locality = request.POST['locality']
        address = request.POST['ads']
        city = request.POST['city']
        state = request.POST['state']
        landmark = request.POST['landmark']

        print(name,number,pincode,locality,address,city,state,landmark)

        Address.objects.create(user=request.user,uname=name,number=number,pincode=pincode,locality=locality,address=address,city=city,state=state,landmark=landmark)
    
    add = Address.objects.filter(user=request.user)
    context = {"address":add}


    return render(request , "manage_add.html",context)


def delete_add(request,id):
    data = Address.objects.get(id=id)
    data.delete()

    return redirect('manage_add')


def edit_add(request,id):
    data = Address.objects.get(id=id)

    if request.method == "POST":
        name = request.POST['uname']
        number = request.POST['number']
        pincode = request.POST['pincode']
        locality = request.POST['locality']
        address = request.POST['ads']
        city = request.POST['city']
        state = request.POST['state']
        landmark = request.POST['landmark']

        data.uname=name
        data.number=number
        data.pincode=pincode
        data.locality=locality
        data.ads=address
        data.city=city
        data.state=state
        data.landmark=landmark
        data.save()
        
        return redirect ('manage_add')
    
    context = {"data":data}

    return render(request , "manage_add.html",context)


login_required(login_url='login')
def payment(request):
    return render(request , "payment.html")