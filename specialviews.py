from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

def displayspecial(request):
    return render(request, 'special.html')