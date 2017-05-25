from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from projects.forms import *
from projects.mixins import ProjectAccessCheckMixin, ProjectMixin


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project

    def get_queryset(self):
        return self.request.user.project_set.all()


class ProjectDetailView(generic.RedirectView):
    # TODO: this should offer and overview of the project.
    def get_redirect_url(self, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return reverse('issues:issue_list', args=[project.pk])


class ProjectCreateView(generic.CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        response = super(ProjectCreateView, self).form_valid(form)

        self.object.members.add(self.request.user)
        self.object.save()

        return response


class ProjectUpdateView(ProjectAccessCheckMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm

    def get_project_kw(self):
        return 'pk'


class ProjectDeleteView(ProjectAccessCheckMixin, generic.DeleteView):
    model = Project

    def get_success_url(self):
        return reverse_lazy('projects:project_list')

    def get_project_kw(self):
        return 'pk'


class ProjectMembershipUpdateView(ProjectMixin, ProjectAccessCheckMixin, generic.UpdateView):
    model = Project
    form_class = ProjectMembersForm
    template_name = 'projects/project_members_form.html'

    def get_project_kw(self):
        return 'pk'


class ProjectReportView(ProjectMixin, ProjectAccessCheckMixin, generic.DetailView):
    model = Project
    template_name = 'projects/project_report.html'

    def get_project_kw(self):
        return 'pk'
