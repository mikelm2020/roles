from django.urls import path

from . import views

app_name = "role_app"

urlpatterns = [
    path(
        "roles/",
        views.RoleListView.as_view(),
        name="role_list",
    ),
    path(
        "rol/<pk>/",
        views.RoleDetailView.as_view(),
        name="role_detail",
    ),
    path(
        "add-rol/",
        views.RoleCreateView.as_view(),
        name="role_add",
    ),
    path(
        "success/",
        views.SuccessView.as_view(),
        name="role_success",
    ),
    path(
        "update-rol/<pk>/",
        views.RoleUpdateView.as_view(),
        name="role_update",
    ),
    path(
        "delete-rol/<pk>/",
        views.RoleDeleteView.as_view(),
        name="role_delete",
    ),
]
