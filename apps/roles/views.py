from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import FormView

from .forms import RoleRegisterForm
from .models import Roles


class RoleListView(LoginRequiredMixin, ListView):
    model = Roles
    template_name = "roles/role_list.html"
    context_object_name = "roles_list"

    paginate_by = 10
    ordering = ["-id"]
    queryset = Roles.objects.all()
    login_url = reverse_lazy("users_app:user_login")


class RoleDetailView(LoginRequiredMixin, DetailView):
    model = Roles
    template_name = "roles/role_detail.html"
    login_url = reverse_lazy("users_app:user_login")


class SuccessView(LoginRequiredMixin, TemplateView):
    template_name = "roles/success.html"
    login_url = reverse_lazy("users_app:user_login")


class RoleCreateView(LoginRequiredMixin, FormView):
    form_class = RoleRegisterForm
    template_name = "roles/add.html"
    success_url = reverse_lazy("role_app:role_success")
    login_url = reverse_lazy("users_app:user_login")

    def form_valid(self, form):
        Roles.objects.create(
            name=form.cleaned_data["name"],
            menu=form.cleaned_data["menu"],
        )
        return super(RoleCreateView, self).form_valid(form)


class RoleUpdateView(LoginRequiredMixin, UpdateView):
    model = Roles
    template_name = "roles/update.html"
    fields = [
        "name",
        "menu",
    ]
    success_url = reverse_lazy("role_app:role_success")
    login_url = reverse_lazy("users_app:user_login")


class RoleDeleteView(LoginRequiredMixin, DeleteView):
    model = Roles
    template_name = "roles/delete.html"
    success_url = reverse_lazy("role_app:role_success")
    login_url = reverse_lazy("users_app:user_login")
