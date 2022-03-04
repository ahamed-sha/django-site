from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProfileInfo

modelform = forms.ModelForm
class UserForm(modelform):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(modelform):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

