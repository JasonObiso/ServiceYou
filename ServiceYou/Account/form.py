from django.forms import ModelForm
from django import forms
from .models import Client


class AccountForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput)
    middlename = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    phonenumber = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)
    address = forms.CharField(widget=forms.TextInput)


