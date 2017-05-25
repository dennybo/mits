from django import forms

from tags.models import *


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color']
