from django.shortcuts import redirect
from django.views import generic

from projects.mixins import ProjectMixin, ProjectAccessCheckMixin
from checklists.forms import *


class ChecklistListView(ProjectMixin, ProjectAccessCheckMixin, generic.ListView):
    def get_context_data(self, **kwargs):
        context = super(ChecklistListView, self).get_context_data(**kwargs)
        context['active'] = 'checklists'
        context['project'] = self.get_project()
        return context

    def get_queryset(self):
        return self.get_project().checklist_set.all()


class ChecklistDetailView(ProjectMixin, ProjectAccessCheckMixin, generic.DetailView):
    model = Checklist

    def get_context_data(self, **kwargs):
        context = super(ChecklistDetailView, self).get_context_data(**kwargs)
        context['add_issue_form'] = ChecklistIssuesForm(instance=self.object)
        return context


class ChecklistCreateView(ProjectMixin, ProjectAccessCheckMixin, generic.CreateView):
    model = Checklist
    form_class = ChecklistForm

    def form_valid(self, form):
        form.instance.project = self.get_project()
        return super(ChecklistCreateView, self).form_valid(form)


class ChecklistUpdateView(ProjectMixin, ProjectAccessCheckMixin, generic.UpdateView):
    model = Checklist
    form_class = ChecklistForm


class ChecklistDeleteView(ProjectMixin, ProjectAccessCheckMixin, generic.DeleteView):
    model = Checklist

    def get_success_url(self):
        return self.get_project().get_checklists_url()


class ChecklistAddIssueView(ProjectMixin, ProjectAccessCheckMixin, generic.DetailView):
    model = Checklist

    def post(self, request, *args, **kwargs):
        checklist = self.get_object()
        form = ChecklistIssuesForm(request.POST, instance=checklist)

        if form.is_valid():
            form.save()

        return redirect(checklist.get_absolute_url())
