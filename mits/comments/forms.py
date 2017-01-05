from django import forms

from models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
