from django.db import models
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.

class Register(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(validators=[validate_email], required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

