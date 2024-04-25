from django.db import models

from apps.abstracts.models import AbstractModel


class Menu(AbstractModel):
    """
      It is a new model for menu
    Args:
        name ( str ): name of the menu
    """

    name = models.CharField(max_length=150, null=False)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.name


class OptionMenu(AbstractModel):
    """
      It is a new model for option menu
    Args:
        name ( str ): name of the option menu
        menu_id ( str ): menu of the option menu
    """

    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=150, null=False)

    class Meta:
        verbose_name = "Opción de menu"
        verbose_name_plural = "OPciones de menu"

    def __str__(self):
        return f"<{self.menu_id.name},{self.name}>"
