from django import forms

from .models import Location


class PostForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location', )

