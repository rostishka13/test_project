
from .models import Groups, List_of_Users
from django.views.generic import ListView, CreateView, DeleteView

# Create your views here.
class HomeView(ListView):
    model = List_of_Users
    template_name = 'base/home.html'
class UsersView(ListView):
    model = List_of_Users
    context_object_name = 'users'
    template_name = 'base/users.html'
class GroupView(ListView):
    model = List_of_Users
    template_name = 'base/groups.html'
    context_object_name = 'groups'
