from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy("users_app:user_login")


# class MixinDate(object):

#     def get_context_data(self, **kwargs):
#         context = super(MixinDate, self).get_context_data(**kwargs)
#         context["now"] = datetime.datetime.now()
#         return context
