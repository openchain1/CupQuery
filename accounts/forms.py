from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserProfileForm(forms.ModelForm):
    bio = forms.Textarea()
    location = forms.CharField(max_length=15, required=False)
    birth_date = forms.DateField(help_text='Format: YYYY-MM-DD', required=False)
    avatar = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'location', 'avatar']


class UserEditForm(forms.ModelForm):
    class Meta(SignUpForm.Meta):
        fields = SignUpForm.Meta.fields
        exclude = ['password']
