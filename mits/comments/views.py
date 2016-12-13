from django.urls import reverse
from django.views import generic

from issues import mixins
from models import *
from forms import *


class CommentCreateView(mixins.IssueMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.issue = self.get_issue()
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('issues:issue_detail', args=[self.get_issue().project.pk, self.get_issue().pk])


class CommentUpdateView(mixins.IssueMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('issues:issue_detail', args=[self.get_issue().project.pk, self.get_issue().pk])


class CommentDeleteView(mixins.IssueMixin, generic.DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('issues:issue_detail', args=[self.get_issue().project.pk, self.get_issue().pk])
