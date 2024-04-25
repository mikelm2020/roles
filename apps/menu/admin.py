from django.contrib import admin

from .models import Menu, OptionMenu


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "base_url",
    )
    search_fields = (
        "id",
        "name",
    )
    ordering = ("id",)


class OptionMenuAdmin(admin.ModelAdmin):
    list_display = (
        "menu",
        "id",
        "name",
        "link_url",
    )
    search_fields = (
        "id",
        "name",
    )
    ordering = ("id",)


admin.site.register(Menu, MenuAdmin)
admin.site.register(OptionMenu, OptionMenuAdmin)
