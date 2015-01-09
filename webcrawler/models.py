from django.db import models
from django import forms
# Create your models here.

class GmailForm(forms.Form):
    inputEmail=forms.EmailField(required=True)
    inputPassword=forms.CharField(required=True)
    