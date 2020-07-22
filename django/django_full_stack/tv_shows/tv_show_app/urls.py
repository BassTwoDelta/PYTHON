from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.allShows),
    path('shows/new', views.newShow),
    path('shows/create', views.createShow),
    path('shows/<num>', views.showPage),
    path('shows/<num>/edit', views.edit),
    path('shows/<num>/update', views.editShow),
    path('shows/<num>/destroy', views.destroyShow)
]