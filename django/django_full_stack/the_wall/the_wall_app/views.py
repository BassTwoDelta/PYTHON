from django.shortcuts import render, redirect
from .models import messages, comments
from login_reg_app.models import User


# Create your views here.
def index(request): 
    user_id = request.session['userid']
    context = {
        "user": User.objects.get(id=user_id),
        "allmessages": messages.objects.all(),
        "all_comment": comments.objects.all()
    }
    return render(request, "the_wall.html", context)

def postMessage(request):
    user_id = request.session['userid']
    ID = User.objects.get(id=user_id)
    messages.objects.create(message=request.POST['message_post'], user=ID)
    return redirect('/wall')

def postComment(request):
    user_id = request.session['userid']
    ID = User.objects.get(id=user_id)
    print(request.POST['comment'])
    comments.objects.create(comment=request.POST['comment'], user=ID, message=messages.objects.get(id=request.POST['message_id']))
    return redirect('/wall')
