from django.urls import path
from . import views

urlpatterns=[
    path("fashion_home",views.index,name="Fashion"),
    path("Men_Footwear",views.Men_Footwear,name="Men_Footwear"),
    path("Mens_Bottom_Wear",views.Mens_Bottom_Wear,name="Mens_Bottom_Wear"),
    path("Mens_Top_Wear",views.Mens_Top_Wear,name="Mens_Top_Wear"),
    path("Women_Ethnic",views.Women_Ethnic,name="Women_Ethnic"),
    path("Women_Footwear",views.Women_Footwear,name="Women_Footwear"),
    path("kids",views.kids,name="kids"),
    
    path("Details/<int:id>",views.display_details,name="f_details"),
]