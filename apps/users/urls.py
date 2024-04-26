from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        "usuarios/",
        views.UserListView.as_view(),
        name="user_list",
    ),
    path(
        "usuario/<pk>/",
        views.UserDetailView.as_view(),
        name="user_detail",
    ),
    path(
        "add-usuario/",
        views.UserCreateView.as_view(),
        name="user_add",
    ),
    path(
        "success/",
        views.SuccessView.as_view(),
        name="user_success",
    ),
    path(
        "update-user/<pk>/",
        views.UserUpdateView.as_view(),
        name="update_user",
    ),
    path(
        "delete-user/<pk>/",
        views.UserDeleteView.as_view(),
        name="delete_user",
    ),
]
