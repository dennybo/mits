from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from projects.models import Project


class ProjectMixin(object):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs[self.get_project_kw()])

    def get_project_kw(self):
        return 'project_pk'


class ProjectAccessCheckMixin(UserPassesTestMixin):
    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs[self.get_project_kw()])
        return project.members.filter(pk=self.request.user.pk).exists()

    def get_project_kw(self):
        return 'project_pk'
