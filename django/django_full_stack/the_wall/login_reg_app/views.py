from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt
from the_wall_app import views
# Create your views here.

def index(request):
    return render(request, 'registration.html')


def registerUser(request):
    errors = User.objects.validator(request.POST)
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    else: 
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        user = User.objects.filter(email=request.POST['email'])
        if user: 
            logged_user = user[0]
            request.session['userid'] = logged_user.id
            userID = request.session['userid']
            ID = User.objects.get(id=userID)
            first_name = ID.first_name
            context = {
            "first_name": first_name
            }
            return redirect('/wall')
    return redirect ("/wall")



def login(request):
    errors  = User.objects.validatorLogin(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    else: 
        user = User.objects.filter(email=request.POST['user_email'])
        logged_user = user[0]
        request.session['userid'] = logged_user.id
        return redirect("/wall")
        



def success(request): 
    userID = request.session['userid']
    ID = User.objects.get(id=userID)
    first_name = ID.first_name
    context = {
        "first_name": first_name
    }
    return render(request, "success.html", context)


def logout(request):
    del request.session['userid']
    return redirect('/')

