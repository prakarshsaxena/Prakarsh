from django import forms
from .models import Dog, MyUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'breed')


class RegistrationForm(UserCreationForm):
    #email = models.EmailField(required=True)

    class Meta:
        model = MyUser
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone',
            'is_staff',
            'is_superuser',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email= self.cleaned_data['email']

        if commit:
            user.save()

        return user


"""
class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = CustomUser
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['username']

class CustomUserChangeForm(UserChangeForm):


    class Meta:
        Model = CustomUser

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['username']
"""