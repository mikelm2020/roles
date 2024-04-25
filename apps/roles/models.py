from django.db import models

from apps.abstracts.models import AbstractModel
from apps.menu.models import Menu


class Roles(AbstractModel):
    """
      It is a new model for roles
    Args:
        name ( str ): name of the role
    """

    name = models.CharField(max_length=15, null=False)
    menu = models.ManyToManyField(Menu, blank=True, null=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name
