from django.urls import path

from . import views

urlpatterns = [
    path("usuarios/", views.UserListView.as_view(), name="user_list"),
    path("usuario/<pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("add-usuario/", views.UserCreateView.as_view(), name="user_add"),
]
