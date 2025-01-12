from django.urls import path
from . import views

urlpatterns=[
    path("AppleProducts",views.AppleProducts,name='AppleProducts'),
    path("SamsungProducts",views.SamsungProducts,name='SamsungProducts'),
    path("RealmeProducts",views.RealmeProducts,name='RealmeProducts'),
    path("PocoProducts",views.PocoProducts,name='PocoProducts'),
    path("OnePlusProducts",views.OnePlusProducts,name='OnePlusProducts'),

]