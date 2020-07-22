from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('learn_more', views.learn_more),
    path('learn_more/boat_deck', views.boat_deck),
    path('learn_more/a_deck', views.a_deck),
    path('learn_more/b_deck', views.b_deck),
    path('learn_more/c_deck', views.c_deck),
    path('learn_more/d_deck', views.d_deck),
    path('learn_more/e_deck', views.e_deck),
    path('learn_more/f_deck', views.f_deck),
    path('learn_more/g_deck', views.g_deck),
    path('learn_more/orlop_deck', views.orlop),
    path('learn_more/tanktop', views.tanktop),
    path('passenger_gen', views.passenger_gen),
    path('passenger_gen/generate', views.generate_passenger),
    path('passenger/passenger_gen/generate', views.generate_passenger),
    path('passenger/<num>', views.passenger),
    path('test', views.test)
]