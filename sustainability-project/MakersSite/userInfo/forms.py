from django import forms
from django.contrib.auth.models import User
from userInfo.models import Category, Page, UserProfile

#http://www.tangowithdjango.com/book17/chapters/login.html
class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('githubURL', 'picture')
