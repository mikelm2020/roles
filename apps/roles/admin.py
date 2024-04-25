from django.contrib import admin

from .models import Roles


class RolesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = (
        "id",
        "name",
    )
    ordering = ("id",)


admin.site.register(Roles, RolesAdmin)
