from django.shortcuts import render, HttpResponse, redirect
from random import randint
from datetime import datetime

def index(request):
    if "gold_count" not in request.session:
        request.session['gold_count'] = 0
    if "activity_log" not in request.session:
        request.session['activity_log'] = []
    return render(request, "index.html")

def process_money(request): 
    print(request.POST)
    if request.POST['location'] == "farm":
        current_time = datetime.now()
        farm_gold = randint(10,20)
        request.session["gold_count"] = request.session["gold_count"] + farm_gold
        activity = (f"EARNED {farm_gold} GOLDS FROM FARM AT {current_time}!!!")
        request.session['activity_log'].append(activity)

    elif request.POST['location'] == "cave":
        current_time = datetime.now()
        cave_gold = randint(5,10)
        request.session["gold_count"] = request.session["gold_count"] + cave_gold
        activity = (f"EARNED {cave_gold} GOLDS FROM CAVE AT {current_time}!!!")
        request.session['activity_log'].append(activity)

    elif request.POST['location'] == "house":
        current_time= datetime.now()
        house_gold = randint(2,5)
        request.session["gold_count"] = request.session["gold_count"] + house_gold
        activity = (f"EARNED {house_gold} GOLDS FROM THE HOUSE {current_time}!!!")
        request.session['activity_log'].append(activity)

    elif request.POST['location'] == "casino":
        current_time= datetime.now()
        casino_gold = randint(-50,50)
        if casino_gold < 0:
            request.session["gold_count"] = request.session["gold_count"] + casino_gold
            activity = (f"LOST {casino_gold} GOLDS FROM THE CASINO AT {current_time}!!")
            request.session['activity_log'].append(activity)
        if casino_gold > 0: 
            request.session["gold_count"] = request.session["gold_count"] + casino_gold
            activity = (f"WON {casino_gold} GOLDS FROM THE CASINO AT {current_time}!!")
            request.session['activity_log'].append(activity)
        if casino_gold == 0: 
            request.session["gold_count"] = request.session["gold_count"] + casino_gold
            activity = (f"BROKE EVEN AT THE CASINO!!! {current_time}!!")
            request.session['activity_log'].append(activity)
    return redirect('/')

def reset(request):
    del request.session['gold_count']
    del request.session['activity_log']
    return redirect('/')