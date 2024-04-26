from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.abstracts.models import AbstractModel
from apps.roles.models import Roles

from .managers import UserManager


class User(PermissionsMixin, AbstractBaseUser, AbstractModel):
    """
      It is a new model for custom user
    Args:
        username ( str ): knick name.
        email ( str ): email of the user
        rol ( str ): role of the user
        is_staff ( bool ): is an user with permissions of the admin panel?
        name ( str ): name of the user
        last_name ( str ): last name of the user
        age ( int ): age of the user
        phone ( str ): phone number of the user
        address ( str ): address of the user

    """

    username = models.CharField(max_length=10, null=False, unique=True)
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
