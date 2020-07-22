from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Item
import bcrypt

# Create your views here.
def index(request):
    return render(request,"login_reg.html")

def dashboard(request):
    user = User.objects.get(id=request.session['userid'])
    my_items = Item.objects.filter(user=user)
    other_items = Item.objects.exclude(user=user)
    name = user.name
    context={
        "name": name,
        "my_items": my_items,
        "logged_in_user": user,
        "other_items": other_items
        }
    return render(request,"dashboard.html", context)

def registerUser(request): 
    errors = User.objects.validator(request.POST)
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    else: 
        User.objects.create(name=request.POST['name'], username=request.POST['username'], password=pw_hash, date_hired=request.POST['date_hired'])
        user = User.objects.filter(username=request.POST['username'])
        if user: 
            logged_user = user[0]
            request.session['userid'] = logged_user.id
            userID = request.session['userid']
            ID = User.objects.get(id=userID)
            name = ID.name
            context = {
            "name": name
            }
            return redirect('/dashboard')
    return redirect ("/dashboard")

def login_user(request):
    errors  = User.objects.validatorLogin(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    else: 
        user = User.objects.filter(username=request.POST['username_login'])
        logged_user = user[0]
        request.session['userid'] = logged_user.id
        return redirect("/dashboard")

def create_item(request):
    return render(request,'create_wish_list.html')

def add_item(request):
    errors = Item.objects.itemValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/wish_items/create")
    else:
        user = request.session['userid']
        ID = User.objects.get(id=user)
        add_item = Item.objects.create(name=request.POST['add_item'], user=ID)
        return redirect('/dashboard')

def item_page(request, num):
    userID = request.session['userid']
    ID = User.objects.get(id=userID)
    other_users = Item.objects.exclude(user=ID)
    context = {
        "item": Item.objects.get(id=num),
        "other_user": other_users,
        "logged_in_user": userID
        
    }
    return render(request, 'wish_list_item.html', context)

def add_to_list(request, num):
    user = User.objects.get(id=request.session['userid'])
    item = Item.objects.get(id=num)
    item.favoritors.add(user)
    item.save()
    return redirect("/dashboard")

def remove_from_list(request, num):
    item = Item.objects.get(id=num)
    user = User.objets.get(id=request.session['userid'])
    item.favoritors.remove(user)
    return redirect("/dashboard")

def delete(request,num):
    item = Item.objects.get(id=num)
    item.delete()
    return redirect('/dashboard')


def logout(request):
    del request.session['userid']
    return redirect('/')