from django.shortcuts import get_object_or_404

from models import Project


class ProjectMixin(object):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs['project_pk'])
