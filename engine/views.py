from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

# regular python function that will not do the job
#def home(request):
#    return ('You are on the home page of the password generator website')

# function with a simple HttpResponse
#def home(request):
#    return ( HttpResponse('You are on the home page of the password generator website') )

# function that renders the view using template
def home(request):
    return ( render(request, 'engine/home.html', {'new_pass': 'tyiogsdfgs78!we'}) )

# we create the new password here - lets test it first
#def password(request):
#    userpass = 'beta-test'
#    return ( render(request, 'engine/password.html', {'newpass': userpass}) )

# function with dynamic content
def password(request):
    pass_set = list(string.ascii_lowercase)
    upercase = list(string.ascii_uppercase)
    specchar = list('!@#$%&*()_+[];:')
    numbers = list('0123456789')
    # passlen = 10 this gave us a static local value, we can also get it from the information
    # the number 10 is the default
    passlen = int(request.GET.get('length'),10)
    if request.GET.get('uppercase'):
        pass_set.extend(upercase)
    if request.GET.get('specchar'):
        pass_set.extend(specchar)
    if request.GET.get('numbers'):
        pass_set.extend(numbers)

    userpass = str()
    for _ in range(passlen):
        userpass += random.choice(pass_set)

    return ( render(request, 'engine/password.html', {'newpass': userpass}) )

# info page
def about(request):
    return ( render(request, 'engine/about.html') )
