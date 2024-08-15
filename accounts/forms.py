from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password',)
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('phonenumber','profile_pic')
        exclude =('user',)
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())