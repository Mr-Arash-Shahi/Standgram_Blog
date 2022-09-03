
from django.contrib.auth.forms import UserChangeForm
from .models import User
from django import forms



class EditForm(UserChangeForm):
    email = forms.EmailField()
    fullname = forms.CharField(max_length=100, widget=forms.TextInput)
    image = forms.FileField()
    class Meta:
        model = User
        fields = ('email', 'fullname', 'image')