from django.db import models
from django.urls import reverse


class Comment(models.Model):
    owner = models.ForeignKey('auth.User')

    issue = models.ForeignKey('issues.Issue')

    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)

    edit_date = models.DateTimeField(auto_now=True)

    def get_update_url(self):
        return reverse('comments:comment_update', args=[self.issue.pk, self.pk])

    def get_delete_url(self):
        return reverse('comments:comment_delete', args=[self.issue.pk, self.pk])
