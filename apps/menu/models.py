from django.db import models

from apps.abstracts.models import AbstractModel


class Menu(AbstractModel):
    """
      It is a new model for menu
    Args:
        name ( str ): name of the menu
        base_url ( str ): base url of the menu
    """

    name = models.CharField(max_length=150, null=False)
    base_url = models.CharField(max_length=100, blank=True, null=True, default="#")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name


class OptionMenu(AbstractModel):
    """
      It is a new model for option menu
    Args:
        menu ( str ): menu of the option menu
        name ( str ): name of the option menu
        link_url ( str ): link url of the option menu

    """

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False)
    link_url = models.CharField(
        max_length=100,
        help_text="URL or URI to the content, eg /about/ or http://opcion.com/",
        blank=True,
        null=True,
        default="#",
    )

    class Meta:
        verbose_name = "Opción de menu"
        verbose_name_plural = "Opciones de menu"

    def __str__(self):
        return f"<{self.menu.name},{self.name}>"
