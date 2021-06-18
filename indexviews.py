from django.http import HttpResponse
from django.shortcuts import render
from shoppingcartproject.indexmodels import indexmodel
from django.contrib import messages

def displayindex(request):
    return render(request, 'index.html')

def showdata(request):
    resultsdisplay = indexmodel.objects.all()
    return render(request, "index.html", {'indexmodel':resultsdisplay})