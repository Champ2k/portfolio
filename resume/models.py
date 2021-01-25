from django.db import models
from django.forms import ModelForm
from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)