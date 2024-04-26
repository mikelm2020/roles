from django import forms

from .models import Roles


class RoleRegisterForm(forms.ModelForm):
    """Form definition for Roles."""

    class Meta:
        """Meta definition for Rolesform."""

        model = Roles
        fields = (
            "name",
            "menu",
        )

    def clean_name(self):
        if Roles.objects.filter(name=self.cleaned_data["name"]).exists():
            raise forms.ValidationError("El rol ya existe")

        if len(self.cleaned_data["name"]) == 0:
            raise forms.ValidationError("El rol no puede estar vacío")

        return self.cleaned_data["name"]

    def clean_menu(self):
        if len(self.cleaned_data["menu"]) == 0:
            raise forms.ValidationError("El menu no puede estar vacío")

        return self.cleaned_data["menu"]
