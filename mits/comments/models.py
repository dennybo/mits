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

    def get_reply_url(self):
        return reverse('comments:reply_create', args=[self.issue.pk, self.pk])


class Reply(models.Model):
    comment = models.ForeignKey('Comment')

    owner = models.ForeignKey("auth.User")

    text = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Replies'

    def get_update_url(self):
        return reverse('comments:reply_update', args=[self.comment.issue.pk, self.comment.pk, self.pk])
