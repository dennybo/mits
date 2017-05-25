from django import forms
from django.forms import inlineformset_factory

from projects.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class ProjectMembersForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['members']
