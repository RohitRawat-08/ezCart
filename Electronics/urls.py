from django.urls import path
from . import views

urlpatterns=[
    path("electronics_home",views.index,name="Electronics"),
    path("Cameras_Accessories",views.Cameras_Accessories,name="Cameras_Accessories"),
    path("HeadPhones",views.HeadPhones,name="HeadPhones"),
    path("laptop_desktop",views.laptop_desktop,name="laptop_desktop"),
    path("Mobile_Accessories",views.Mobile_Accessories,name="Mobile_Accessories"),
    path("Powerbank",views.Powerbank,name="PowerBank"),

    path("Details/<int:id>",views.Electronic_Product_Details,name="Electronic_Product_Details"),
]