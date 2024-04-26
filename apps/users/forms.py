from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):
    """Form definition for User."""

    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Contraseña"},
        ),
    )
    password2 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Repetir Contraseña"},
        ),
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            "username",
            "name",
            "last_name",
            "email",
            "age",
            "phone",
            "address",
            "role",
        )

    def clean_password2(self):
        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            self.add_error("password2", "Las contraseñas no son iguales")

    def clean_password1(self):
        if len(self.cleaned_data["password1"]) < 8:
            # self.add_error("password1", "La contraseña debe tener al menos 8 caracteres")
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres",
            )
        return self.cleaned_data["password1"]

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data["username"]).exists():
            raise forms.ValidationError("El usuario ya existe")

        if len(self.cleaned_data["username"]) == 0:
            raise forms.ValidationError("El usuario no puede estar vacío")

        return self.cleaned_data["username"]

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data["email"]).exists():
            raise forms.ValidationError("El email ya existe")

        if len(self.cleaned_data["email"]) == 0:
            raise forms.ValidationError("El email no puede estar vacío")

        return self.cleaned_data["email"]


class LoginForm(forms.Form):
    username = forms.CharField(
        label="username",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "username",
                "style": "{margin: 10px}",
            },
        ),
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Contraseña"},
        ),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos del usuario no son correctos")

        return cleaned_data


class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Contraseña actual"},
        ),
    )
    password2 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Contraseña nueva"},
        ),
    )

    def clean_password2(self):
        if len(self.cleaned_data["password2"]) < 8:
            # self.add_error("password1", "La contraseña debe tener al menos 8 caracteres")
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres",
            )
        return self.cleaned_data["password2"]


class VerificationForm(forms.Form):
    register_code = forms.CharField(required=True, max_length=6)

    def __init__(self, pk, *args, **kwargs):
        self.user_id = pk
        return super(VerificationForm, self).__init__(*args, **kwargs)

    def clean_register_code(self):
        obtained_code = self.cleaned_data["register_code"]
        if len(obtained_code) == 6:
            # Verficate if the obtained code and the user id are valids
            active = User.objects.validation_of_code(
                self.user_id,
                obtained_code,
            )
            if not active:
                raise forms.ValidationError("El código es incorrecto")
        else:
            raise forms.ValidationError("El código es incorrecto")
