from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random(request):
    counter = request.session.get('counter', 1)
    request.session['counter'] = counter + 1
    random_word = get_random_string(length=12)
    context= {
        'counter': counter,
        'random_word': random_word,
    }
    return render(request,'index.html',context=context)

def reset(request):
    del request.session['counter']
    return redirect("/random_word")
