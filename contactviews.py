from django.http import HttpResponse
from django.shortcuts import render
from shoppingcartproject.contactmodels import contactmodel
from django.contrib import messages

def displaycontact(request):
    return render(request, 'contactus.html')

def insertcontact(request):
    if request.method == 'POST':
        if request.POST.get('fullname')and request.POST.get('email')and request.POST.get('message'):
            saverecord = contactmodel()
            saverecord.fullname = request.POST.get('fullname')
            saverecord.email = request.POST.get('email')
            saverecord.message = request.POST.get('message')
            saverecord.save()
            #messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'contactus.html')
    else:
            return render(request, 'contactus.html')