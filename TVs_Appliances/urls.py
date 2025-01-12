from django.urls import path
from . import views

urlpatterns=[
    path("tv_appliances_home",views.index,name='TvAppliances'),
    path("Air_conditioners",views.Air_conditioners,name='Air_conditioners'),
    path("Refrigerators",views.Refrigerators,name='Refrigerators'),
    path("Televisions",views.Televisions,name='Televisions'),
    path("Washing_machine",views.Washing_machine,name='Washing_machine'),
]