from django import forms

from models import *


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['name', 'description']


class IssueChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return '#%d - %s' % (obj.index, obj.name)


class ChecklistAddIssueForm(forms.Form):
    issue = IssueChoiceField(queryset=None)

    def __init__(self, checklist, *args, **kwargs):
        super(ChecklistAddIssueForm, self).__init__(*args, **kwargs)
        self.fields['issue'].queryset = checklist.project.issue_set.exclude(pk__in=checklist.issues.all()).all()
