from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from models import Project


class ProjectMixin(object):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs['project_pk'])


class ProjectAccessCheckMixin(UserPassesTestMixin):
    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])

        try:
            project.members.filter(project__membership__user=self.request.user).get()
            return True
        except:
            return False
