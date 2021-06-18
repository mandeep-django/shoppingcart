from django.shortcuts import render
from shoppingcartproject.signupmodels import signupmodel
from django.contrib import messages

def displaysignup(request):
    return render(request, 'signup.html')

def insertsignup(request):
    if request.method == 'POST':
        if request.POST.get('fullname')and request.POST.get('email')and request.POST.get('password'):
            saverec = signupmodel()
            saverec.fullname = request.POST.get('fullname')
            saverec.email = request.POST.get('email')
            saverec.password = request.POST.get('password')
            saverec.save()
            #messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'signup.html')
    else:
            return render(request, 'signup.html')