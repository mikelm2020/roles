from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from django.views.generic.edit import FormView

from .forms import LoginForm, UpdatePasswordForm, UserRegisterForm
from .models import User


class UserListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users_list"

    paginate_by = 10
    ordering = ["-id"]
    queryset = User.objects.all()
    login_url = reverse_lazy("users_app:user_login")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/user_detail.html"
    login_url = reverse_lazy("users_app:user_login")


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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/update.html"
    fields = [
        "username",
        "name",
        "last_name",
        "email",
        "age",
        "phone",
        "address",
        "role",
    ]
    success_url = reverse_lazy("users_app:user_success")
    login_url = reverse_lazy("users_app:user_login")


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_app:user_success")
    login_url = reverse_lazy("users_app:user_login")


class Login(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home_app:panel")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(self.request, user)
        return super(Login, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse("users_app:user_login"),
        )


class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = "users/update_password.html"
    form_class = UpdatePasswordForm
    login_url = reverse_lazy("users_app:user_login")

    def form_valid(self, form):
        current_user = self.request.user
        user = authenticate(
            username=current_user.username,
            password=form.cleaned_data["password1"],
        )
        if user:
            new_password = form.cleaned_data["password2"]
            current_user.set_password(new_password)
            current_user.save()

        logout(self.request)
        return super(UpdatePassword, self).form_valid(form)
