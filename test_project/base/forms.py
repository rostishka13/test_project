from django import forms
from .models import List_of_Users, Groups

class AddUserForm(forms.ModelForm):
     class Meta:
        model = List_of_Users
        fields = '__all__'

class AddGroupForm(forms.ModelForm):
     class Meta:
        model = Groups
        fields = '__all__'

class EditUserForm(forms.ModelForm):
     class Meta:
        model = List_of_Users
        fields = '__all__'