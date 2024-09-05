from django import forms
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'text']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
