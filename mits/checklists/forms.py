from django import forms

from models import *


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['name', 'description']


class IssueChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '#%d - %s' % (obj.index, obj.name)


class ChecklistIssuesForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['issues']
