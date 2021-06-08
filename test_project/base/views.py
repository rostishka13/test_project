
from .models import Groups, List_of_Users
from django.views.generic import ListView, CreateView, DeleteView
from .forms import AddUserForm, AddGroupForm
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    model = List_of_Users
    template_name = 'base/home.html'
class UsersView(ListView):
    model = List_of_Users
    context_object_name = 'users'
    template_name = 'base/users.html'

class GroupView(ListView):
    model = Groups
    template_name = 'base/groups.html'
    context_object_name = 'groups'


class AddUserView(CreateView):
    model = List_of_Users
    template_name = 'base/add_users.html'
    form_class = AddUserForm
    success_url = reverse_lazy('users')



class AddGroupView(CreateView):
    model = Groups
    success_url = reverse_lazy('groups')
    template_name = 'base/add_groups.html'
    form_class = AddGroupForm

    
   