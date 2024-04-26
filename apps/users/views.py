from django.views.generic import CreateView, DetailView, ListView

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


class UserCreateView(CreateView):
    model = User
    template_name = "users/add.html"
