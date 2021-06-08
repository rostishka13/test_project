from django.urls import path

from .views import  HomeView,UsersView, GroupView

urlpatterns = [
    path('', HomeView.as_view(),  name='home'),
    path('users/',UsersView.as_view(), name='users'),
    path('groups/', GroupView.as_view() , name='groups'),

    
]