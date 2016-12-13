from django.views import generic

from models import *
from forms import *
from projects import mixins


class IssueDetailView(generic.DetailView):
    model = Issue


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
