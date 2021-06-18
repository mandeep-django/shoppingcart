"""shoppingcartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .import indexviews
from .import buycartviews
from .import signupviews
from .import productviews
from .import contactviews
from .import specialviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexviews.displayindex, name="displayindex"),
    path('', indexviews.showdata, name="showdata"),
    path('signup', signupviews.displaysignup, name="displaysignup"),
    path('signup', signupviews.insertsignup, name="insertsignup"),
    path('contactus', contactviews.displaycontact, name="displaycontact"),
    path('contactus', contactviews.insertcontact, name="insertcontact"),
    path('products', productviews.displayproduct, name="displayproduct"),
    path('buycart', buycartviews.displaybuycart, name="displaybuycart"),
    path('special', specialviews.displayspecial, name="displayspecial"),
]
