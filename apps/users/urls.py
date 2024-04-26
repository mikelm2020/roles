from django.urls import path

from . import views

urlpatterns = [
    path("usuarios/", views.UserListView.as_view(), name="usuarios"),
]
