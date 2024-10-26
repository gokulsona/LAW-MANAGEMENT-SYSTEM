from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ()

        labels={
            'name':'Enter Name',
            'phone':'Enter Phone',
            'email':'Enter Email',
            'password':'Enter Password',
            'confirm_password':'confirm your password'
        }





