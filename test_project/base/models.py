from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse
from multiselectfield import MultiSelectField
# Create your models here.

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

class List_of_Users(models.Model):

    first_name = models.CharField(max_length=120,blank=True, null=True)
    last_name = models.CharField(max_length=120,blank=True, null=True)
    username = models.CharField(max_length=120,help_text='Input you nickname')
    email = models.EmailField(blank=True, null=True)
    group= models.ForeignKey('Groups', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name)


    class Meta:
        verbose_name_plural = 'List of Users'
        ordering = ['-created']

    

class Groups(models.Model):
    group = models.CharField(max_length=120)

    description = MultiSelectField(choices=CHOICES)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name_plural = 'Groups'
    
