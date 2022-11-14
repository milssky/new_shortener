from django.urls import path

from . import views


app_name = "shortener"

urlpatterns = [
    path("", views.index, name="index"),
    path("go/<slug:slug>", views.url_detail, name="go"),
]
