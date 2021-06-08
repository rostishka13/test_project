from django.db import models
from django.urls import reverse
# Create your models here.


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
    description = models.TextField()

    def __str__(self):
        return self.group

    class Meta:
        verbose_name_plural = 'Groups'
    
