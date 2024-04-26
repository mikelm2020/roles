from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import FormView

from .forms import UserRegisterForm
from .models import User


class UserListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users_list"
    paginate_by = 10
    ordering = ["-id"]
    queryset = User.objects.all()


class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"


class SuccessView(TemplateView):
    template_name = "users/success.html"


class UserCreateView(FormView):
    template_name = "users/add.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_app:user_success")

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password1"],
            name=form.cleaned_data["name"],
            last_name=form.cleaned_data["last_name"],
            age=form.cleaned_data["age"],
            phone=form.cleaned_data["phone"],
            address=form.cleaned_data["address"],
            role=form.cleaned_data["role"],
        )
        return super(UserCreateView, self).form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/update.html"
    fields = [
        "name",
        "menu",
    ]
    success_url = reverse_lazy("users_app:user_success")


class UserDeleteView(DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_app:user_success")
