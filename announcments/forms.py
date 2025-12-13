from django import forms

from .models import Announcement

class AnnouncmentForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'