from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.registerUser),
    path('login_user', views.login_user),
    path('dashboard', views.dashboard),
    path('wish_items/create', views.create_item),
    path('wish_items/create/add_item', views.add_item),
    path('wish_items/<num>', views.item_page),
    path('wish_items/<num>/add_to_list', views.add_to_list),
    path('wish_items/<num>/remove', views.remove_from_list),
    path('wish_items/<num>/delete', views.delete),
    path('logout', views.logout)
]