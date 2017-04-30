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
    issues = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        super(ChecklistIssuesForm, self).__init__(*args, **kwargs)
        self.fields['issues'].queryset = self.instance.project.issue_set

    class Meta:
        model = Checklist
        fields = ['issues']
