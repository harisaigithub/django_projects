from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsregForm(UserCreationForm):
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control my-2", "placeholder":"Enter Password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control my-2", "placeholder":"Enter Password"}))
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username":forms.TextInput(
               attrs={"class":"form-control my-2", "placeholder":"Username",} 
            )
        }