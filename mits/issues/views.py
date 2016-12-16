from django.views import generic
import services

from forms import *
from projects import mixins
from comments.forms import CommentForm


class IssueListView(mixins.ProjectMixin, mixins.ProjectAccessCheckMixin, generic.ListView):
    model = Issue

    def get_context_data(self, **kwargs):
        project = self.get_project()

        context = super(IssueListView, self).get_context_data(**kwargs)
        context['active'] = 'issues'
        context['project'] = project
        context['membership'] = project.get_membership(self.request.user)

        return context


class IssueDetailView(mixins.ProjectMixin, mixins.ProjectAccessCheckMixin, generic.DetailView):
    model = Issue

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['tags'] = services.pack_issue_tags(self.object)
        return context


class IssueCreateView(mixins.ProjectMixin, mixins.ProjectAccessCheckMixin, generic.CreateView):
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


class IssueUpdateView(mixins.ProjectAccessCheckMixin, generic.UpdateView):
    model = Issue
    form_class = IssueForm


class IssueTagsUpdateView(mixins.ProjectAccessCheckMixin, generic.UpdateView):
    model = Issue
    form_class = IssueTagsForm

    def get_success_url(self):
        return self.object.get_absolute_url()
