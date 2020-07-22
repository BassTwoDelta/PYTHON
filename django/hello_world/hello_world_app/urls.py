from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('nba', views.nbaPage),
    path('teams', views.nbaTeams),
    path('teams/<int:teamId>', views.showAteam),
    path('logout', views.logout),
]
