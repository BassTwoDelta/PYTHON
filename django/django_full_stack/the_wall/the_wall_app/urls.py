from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('/post_message', views.postMessage),
    path('/post_comment', views.postComment),
]