from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from issues import mixins
from comments.models import *
from comments.forms import *


class CommentCreateView(mixins.IssueMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.issue = self.get_issue()
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.get_issue().get_absolute_url()


class CommentUpdateView(mixins.IssueMixin, generic.UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return self.get_issue().get_absolute_url()


class CommentDeleteView(mixins.IssueMixin, generic.DeleteView):
    model = Comment

    def get_success_url(self):
        return self.get_issue().get_absolute_url()


class ReplyCreateView(mixins.IssueMixin, generic.CreateView):
    model = Reply
    form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(ReplyCreateView, self).get_context_data(**kwargs)
        context['comment'] = self.get_comment()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.comment = self.get_comment()
        return super(ReplyCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.get_issue().get_absolute_url()

    def get_comment(self):
        return get_object_or_404(Comment, pk=self.kwargs['comment_pk'])


class ReplyUpdateView(mixins.IssueMixin, generic.UpdateView):
    model = Reply
    form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(ReplyUpdateView, self).get_context_data(**kwargs)
        context['comment'] = self.get_comment()
        return context

    def get_success_url(self):
        return self.get_issue().get_absolute_url()

    def get_comment(self):
        return get_object_or_404(Comment, pk=self.kwargs['comment_pk'])

