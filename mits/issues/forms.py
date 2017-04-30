from django import forms
from django.forms import widgets

from models import *


class IssueForm(forms.ModelForm):
    checklists = forms.ModelMultipleChoiceField(
        queryset=None, required=False, widget=widgets.SelectMultiple(attrs={
            'class': 'selectpicker',
            'data-live-search': 'true',
            'multiple': 'multiple'
        }))

    def __init__(self, project, issue, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        # configure checklists field.
        self.fields['checklists'].queryset = project.checklist_set
        if issue:
            self.fields['checklists'].initial = issue.checklist_set.all()

    class Meta:
        model = Issue
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super(IssueForm, self).save(commit)

        # save checklists.
        instance.checklist_set.clear()
        for checklist in self.cleaned_data['checklists']:
            checklist.issues.add(instance)

        return instance


class IssueTagsForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['tags']
