from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.user_list, name="users"),
    path("users/create", views.user_create, name="user_create"),
    path("users/store", views.user_store, name="user_store"),
]