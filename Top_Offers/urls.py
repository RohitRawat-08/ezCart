from django.urls import path
from . import views

urlpatterns=[
    path("Top_offers_home",views.index,name="Offers"),
    path("Details/<int:id>",views.display_details,name="d_details")
]