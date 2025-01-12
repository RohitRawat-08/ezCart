from django.urls import path
from . import views

urlpatterns=[
    path("login_page",views.index,name='login'),
    path("New_Registration",views.New_Registration,name='New_Registration'),
    path("logout_",views.logout_,name='logout'),

    path("profile",views.profile,name='profile'),
    path("profile_info",views.profile_info,name='profile_info'),
    path("manage_add",views.manage_add,name='manage_add'),
    path("payment",views.payment,name='payment'),

    path("my_order/<str:model_name>/<int:id>",views.my_order,name='my_order'),
    path("place_order_f_cart",views.place_order_f_cart,name='place_order_f_cart'),

    path("my_orders",views.my_order_list,name='my_orders_list'),
    path("add_profile_img",views.add_profile_img,name='add_profile_img'),


    path("delete_add/<int:id>",views.delete_add,name='delete_add'),
    path("edit_add/<int:id>",views.edit_add,name='edit_add'),
]