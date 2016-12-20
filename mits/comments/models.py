from django.db import models
from django.urls import reverse
from issues.models import Event


class Comment(Event):
    text = models.TextField()

    edit_date = models.DateTimeField(auto_now=True, null=True)

    def get_update_url(self):
        return reverse('comments:comment_update', args=[self.issue.pk, self.pk])

    def get_delete_url(self):
        return reverse('comments:comment_delete', args=[self.issue.pk, self.pk])
