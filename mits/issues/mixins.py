from django.shortcuts import get_object_or_404

from issues.models import Issue
from projects.mixins import ProjectMixin


class IssueMixin(ProjectMixin):
    def get_issue(self):
        return get_object_or_404(Issue, pk=self.kwargs['issue_pk'])
