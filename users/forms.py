__author__ = 'Suy'
from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'uname','id':'username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class':'youpasswd','id':'password','data-icon':'p'}))

    def clean(self):
        try:
            user = User.objects.get(username=self.cleaned_data.get('username'))
            if not user.check_password(self.cleaned_data.get('password')):
                raise ValidationError(
                    "Your username or password is incorrect"
                )
        except User.DoesNotExist:
            raise ValidationError(
                "Your user not exist contact the administration to add an account for you"
            )
        return self.cleaned_data


