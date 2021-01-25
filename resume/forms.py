from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': '',
            'email': '',
            'message': '',
        }
        widgets = {
            'name': forms.TextInput(
                    attrs={'class':'form-control',
                            'placeholder':'Name',
                            }
            ),
            'email': forms.TextInput(
                    attrs={'class':'form-control',
                            'placeholder':'Email',
                            }
            ),
            'message':forms.Textarea(
                        attrs={'class':'form-control',
                            'placeholder':'Subject'
                            }
                        ),
        }