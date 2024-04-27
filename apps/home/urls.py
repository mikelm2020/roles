from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        "",
        views.HomePage.as_view(),
        name="home",
    ),
    path(
        "panel",
        views.Panel.as_view(),
        name="panel",
    ),
]
