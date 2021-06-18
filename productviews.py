from django.http import HttpResponse
from django.shortcuts import render
from shoppingcartproject.productmodels import productmodel
from django.contrib import messages

def displayproduct(request):
    return render(request, 'products.html')