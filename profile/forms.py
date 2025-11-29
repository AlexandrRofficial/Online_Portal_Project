from django import forms
from .models import profile, post

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ["post"]