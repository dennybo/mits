from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django import views
import services

from models import *
from forms import *
from projects import mixins
from comments.forms import CommentForm
from tags.models import *


class IssueListView(mixins.ProjectMixin, generic.ListView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        context['active'] = 'issues'
        context['project'] = self.get_project()
        return context


class IssueDetailView(generic.DetailView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['tags'] = services.pack_issue_tags(self.object)
        return context


class IssueCreateView(mixins.ProjectMixin, generic.CreateView):
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        project = self.get_project()

        form.instance.owner = self.request.user
        form.instance.project = project

        form.instance.index = project.issue_index

        project.issue_index += 1
        project.save()

        return super(IssueCreateView, self).form_valid(form)


class IssueUpdateView(generic.UpdateView):
    model = Issue
    form_class = IssueForm


class IssueTagsUpdateView(generic.UpdateView):
    model = Issue
    form_class = IssueTagsForm

    def get_success_url(self):
        return self.object.get_absolute_url()
