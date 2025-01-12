"""
URL configuration for EZcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('home.urls')),
    
    path('Cart/',include('Cart.urls')),
    path('Electronics/',include('Electronics.urls')),
    path('Fashion/',include('Fashion.urls')),
    path('Log_In/',include('Log_In.urls')),
    path('Mobiles_Tab/',include('Mobiles_Tab.urls')),
    path('Top_Offers/',include('Top_Offers.urls')),
    path('TVs_Appliances/',include('TVs_Appliances.urls')),

    path("__reload__/",include("django_browser_reload.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)