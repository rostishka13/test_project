from django.urls import path

from .views import  HomeView,UsersView, GroupView, AddUserView,AddGroupView, EditUserView, DeleteUserView, EditGroupView,DeleteGroupView

urlpatterns = [
    # path('', HomeView.as_view(),  name='home'),
    path('',UsersView.as_view(), name='users'),
    path('groups/', GroupView.as_view() , name='groups'),

    path('add_user/', AddUserView.as_view(), name='add_user'),
    path('add_group/', AddGroupView.as_view(), name='add_group'),

    path('edit/user/<int:pk>/', EditUserView.as_view(), name='edit_user'),
    path('delete/user/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),

    path('edit/group/<int:pk>',EditGroupView.as_view(), name='edit_group' ),
    path('delete/group/<int:pk>/', DeleteGroupView.as_view(), name='delete_group'),



]