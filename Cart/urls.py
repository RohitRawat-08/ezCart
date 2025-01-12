from django.urls import path
from . import views

urlpatterns=[

    path("cart_items",views.index,name='cart'),

    path("add_cart/<str:model_name>/<int:id>",views.add_cart,name='add_cart'),
    path("buy/<str:model_name>/<int:id>",views.buy,name='buy'),

    path("remove_cart_itm/<int:id>",views.remove_cart_itm,name='remove_cart_itm'),

]