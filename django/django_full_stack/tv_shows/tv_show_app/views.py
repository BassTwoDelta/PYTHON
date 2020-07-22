from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Shows

# Create your views here.
def index(request):
    return redirect("/shows")

def allShows(request): 
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, "shows.html", context)

def newShow(request):
    return render(request, "newshow.html")

def createShow(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else: 
        Shows.objects.create(title=request.POST['title'], network=request.POST['network'],release_date=request.POST['release_date'], description=request.POST['description'])
        show = Shows.objects.get(title=request.POST['title'])
        num = show.id
        messages.success(request,"Show officially added")

    return redirect(f"/shows/{num}")

def showPage(request,num):
    context = {
        "show": Shows.objects.get(id=num)
    }
    return render(request,"showpage.html",context)

def edit(request, num):
    context = {
        "show": Shows.objects.get(id=num)
    }
    return render(request, "editshow.html", context)

def editShow(request, num):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{num}/edit")
    else: 
        show = Shows.objects.get(id=num)
        show.title= request.POST['title']
        show.network= request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        num = show.id
    return redirect(f"/shows/{num}")

def destroyShow(request,num):
    show = Shows.objects.get(id=num)
    show.delete()
    return redirect("/shows")

    
