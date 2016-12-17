from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from models import *
from forms import *
from projects.mixins import ProjectAccessCheckMixin, ProjectMixin


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(membership__user=self.request.user)


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

        membership = Membership(project=self.object, user=self.request.user, is_administrator=True)
        membership.save()

        return response


class ProjectUpdateView(generic.UpdateView):
    model = Project
    form_class = ProjectForm


class ProjectDeleteView(ProjectAccessCheckMixin, generic.DeleteView):
    model = Project

    def get_success_url(self):
        return reverse_lazy('projects:project_list')

    def get_project_kw(self):
        return 'pk'


class ProjectMembershipUpdateView(ProjectMixin, ProjectAccessCheckMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_members_form.html'

    def get(self, request, *args, **kwargs):
        project = self.get_object()

        return self.render_to_response({
            'form': ProjectMembersFormSet(instance=project)
        })

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        formset = ProjectMembersFormSet(self.request.POST, instance=project)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(project.get_absolute_url())

        self.render_to_response(self.get_context_data(form=formset))

    def get_project_kw(self):
        return 'pk'
