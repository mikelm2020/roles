from django.views.generic import ListView

from .models import User


class UserListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users_list"
    paginate_by = 10
    ordering = ["-id"]
    queryset = User.objects.all()
