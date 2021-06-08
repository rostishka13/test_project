
from typing import Callable
from django.db import models
from django.views.generic.edit import UpdateView
from .models import Groups, List_of_Users
from django.views.generic import ListView, CreateView, DeleteView
from .forms import AddUserForm, AddGroupForm, EditUserForm,EditGroupForm
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse


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


class EditUserView(UpdateView):
    model = List_of_Users
    form_class = EditUserForm
    success_url = reverse_lazy('users')
    template_name = 'base/edit_user.html'

class DeleteUserView(DeleteView):
    model = List_of_Users
    success_url = reverse_lazy('users')
    template_name = 'base/delete_user.html'




class EditGroupView(UpdateView):
    model = Groups
    form_class = EditGroupForm
    success_url = reverse_lazy('groups')
    template_name = 'base/edit_group.html'   


class DeleteGroupView(DeleteView):
    model = Groups
    success_url = reverse_lazy('groups')
    template_name = 'base/delete_group.html'



   