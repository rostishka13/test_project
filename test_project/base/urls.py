from django.urls import path

from .views import  HomeView,UsersView, GroupView, AddUserView,AddGroupView

urlpatterns = [
    path('', HomeView.as_view(),  name='home'),
    path('users/',UsersView.as_view(), name='users'),
    path('groups/', GroupView.as_view() , name='groups'),

    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('add_group/', AddGroupView.as_view(), name='add_group'),


]