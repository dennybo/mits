from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

from models import Project, Membership


class ProjectMixin(object):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs[self.get_project_kw()])

    def get_project_kw(self):
        return 'project_pk'


class ProjectAccessCheckMixin(UserPassesTestMixin):
    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs[self.get_project_kw()])

        try:
            Membership.objects.filter(project=project, user=self.request.user).get()
            return True
        except:
            return False

    def get_project_kw(self):
        return 'project_pk'
