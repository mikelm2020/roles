from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "is_active",
        "email",
        "is_staff",
        "role",
        "name",
        "last_name",
        "age",
        "phone",
        "address",
    )
    search_fields = (
        "id",
        "username",
        "role",
        "age",
    )
    ordering = ("id",)


admin.site.register(User, UserAdmin)
