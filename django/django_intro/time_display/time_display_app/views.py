from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    current_date_time = datetime.now()
    context = {
        'currentTime': current_date_time
    }
    return render(request, 'index.html', context)