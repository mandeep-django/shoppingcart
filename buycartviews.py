from django.http import HttpResponse
from django.shortcuts import render
from shoppingcartproject.buycartmodels import buycartmodel
from django.contrib import messages

def displaybuycart(request):
    return render(request, 'buycart.html')