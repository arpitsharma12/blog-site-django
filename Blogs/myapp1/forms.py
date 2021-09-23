from django import forms
from django.db import models
from django.forms import fields
from . models import Blog

class Edit_Blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields=('title','dsc')
           