from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

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


class RoleCreateView(CreateView):
    model = Roles
    template_name = "roles/add.html"
    fields = [
        "name",
        "menu",
    ]
    success_url = reverse_lazy("role_app:role_success")
