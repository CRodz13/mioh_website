from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.home, name="contact"),
    path("store/", views.home, name="store"),
]
