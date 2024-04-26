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


class RoleListView(ListView):
    model = Roles
    template_name = "roles/roles_list.html"
    context_object_name = "roles_list"
    paginate_by = 10
    ordering = ["-id"]
    queryset = Roles.objects.all()


class RoleDetailView(DetailView):
    model = Roles
    template_name = "roles/role_detail.html"


class SuccessView(TemplateView):
    template_name = "roles/success.html"


class RoleCreateView(FormView):
    form_class = RoleRegisterForm
    template_name = "roles/add.html"
    success_url = reverse_lazy("role_app:role_success")

    def form_valid(self, form):
        Roles.objects.create(
            name=form.cleaned_data["name"],
            menu=form.cleaned_data["menu"],
        )
        return super(RoleCreateView, self).form_valid(form)


class RoleUpdateView(UpdateView):
    model = Roles
    template_name = "roles/update.html"
    fields = [
        "name",
        "menu",
    ]
    success_url = reverse_lazy("role_app:role_success")


class RoleDeleteView(DeleteView):
    model = Roles
    template_name = "roles/delete.html"
    success_url = reverse_lazy("role_app:role_success")
