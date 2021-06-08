from django import forms
from .models import List_of_Users, Groups

CHOICES = (
    ('#1', 'Data Analytics'),
    ('#2', 'Services Analytics'),
    ('#3', 'Voice Analytics'),
    ('#4', 'Queue Stats'),
    ('#5', 'Voice Stats'),
    ('#6', 'Video Stats'),
    ('#7', 'Smart Access'),
    ('#8', 'Diagrams'),  
)               



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


class EditGroupForm(forms.ModelForm):
     class Meta:
        model = Groups
        fields = '__all__'
