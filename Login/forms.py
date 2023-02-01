from dataclasses import fields
from tkinter import Label, Widget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

class RegistrtionForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']  #if writing the fields with capital letter then throws error.
        labels = {'username':'UserName','first_name':'First_Name','last_name':'Last_Name','email': 'Email'} #suppose First_Name, then it throws error  
       
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password= forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

# This Validation will be usefull when we create our own custom Login NOT Django buil-in Login system
# def clean_username(self):
#     username = self.cleaned_data["username"]
#     try:
#         User.objects.get(username=username)
#     except User.DoesNotExist:
#         return username
#     raise forms.ValidationError(("A user with that username already exists."))

# def clean_password2(self):
#     password1 = self.cleaned_data.get("password1", "")
#     password2 = self.cleaned_data["password2"]
#     if password1 != password2:
#         raise forms.ValidationError(("The two password fields didn't match."))
#     return password2

# def save(self, commit=True):
#     user = super(UserCreationForm, self).save(commit=False)
#     user.set_password(self.cleaned_data["password1"])
#     if commit:
#         user.save()
#     return user