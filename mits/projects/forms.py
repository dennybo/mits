from django import forms
from django.forms import inlineformset_factory

from models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class ProjectMembersForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['members']


ProjectMembersFormSet = inlineformset_factory(
    Project, Membership, fields=('user', 'is_administrator'),
    labels={
        'is_administrator': '',
        'DELETE': '',
    }
)
