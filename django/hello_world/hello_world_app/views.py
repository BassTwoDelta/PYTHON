from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request): #every function needs keyword "request"
    now = datetime.now()
    print(now)
    context = {
        'currentTime': now
    }
    return render(request, 'index.html', context)

def nbaPage(request): 
    return HttpResponse ('Here is the NBA page')

def nbaTeams(request):
    return HttpResponse ('Placeholder for NBA teams')

def showAteam(request, teamId):
    return HttpResponse (f"placeholder to show info on team number {teamId}")

def logout(request):
    return redirect('/')