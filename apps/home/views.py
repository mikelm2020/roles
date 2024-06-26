from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home/index.html"


class Panel(LoginRequiredMixin, TemplateView):
    template_name = "home/panel.html"
    login_url = reverse_lazy("users_app:user_login")
