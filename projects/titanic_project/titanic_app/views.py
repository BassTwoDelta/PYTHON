from django.shortcuts import render, redirect
from .models import TitanicPassengers
import random

# Create your views here.
def index(request):
    return render(request, "index.html")

def learn_more(request):
    return render(request, "learn_more.html")

def boat_deck(request):
    return render(request, "boat_deck.html")

def a_deck(request):
    return render(request, "a_deck.html")

def b_deck(request):
    return render(request, "b_deck.html")

def c_deck(request):
    return render(request, "c_deck.html")

def d_deck(request):
    return render(request, "d_deck.html")

def e_deck(request):
    return render(request, "e_deck.html")

def f_deck(request):
    return render(request, "f_deck.html")

def g_deck(request):
    return render(request, "g_deck.html")

def orlop(request):
    return render(request, "orlop_deck.html")

def tanktop(request):
    return render(request, "tanktop.html")

def test(request): 
    return render(request, "new_text_index.html")

def passenger_gen(request):
    context = {
        "passengers": TitanicPassengers.objects.all()
    }
    return render(request, "passenger_gen.html")

def generate_passenger(request):
    passenger_id = random.randint(0,2175)
    passenger = TitanicPassengers.objects.get(id=passenger_id)
    return redirect(f'/passenger/{passenger_id}')

def passenger(request, num):
    context = {
        "passenger": TitanicPassengers.objects.get(id=num)
    }
    return render(request, "passenger.html", context)
