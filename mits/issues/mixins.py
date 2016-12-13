from django.shortcuts import get_object_or_404

from models import Issue


class IssueMixin(object):
    def get_issue(self):
        return get_object_or_404(Issue, pk=self.kwargs['issue_pk'])
