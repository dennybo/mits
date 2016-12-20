from django.db import models
from django.urls import reverse


class Issue(models.Model):
    project = models.ForeignKey('projects.Project')

    owner = models.ForeignKey('auth.User')

    name = models.CharField(max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)

    description = models.TextField(blank=True)

    index = models.IntegerField()

    tags = models.ManyToManyField('tags.Tag', blank=True)

    # this is controlled by IssueStates.
    closed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('issues:issue_detail', args=[self.project.pk, self.pk])

    def get_update_url(self):
        return reverse('issues:issue_update', args=[self.project.pk, self.pk])

    def get_close_url(self):
        return reverse('issues:issue_close', args=[self.project.pk, self.pk])

    def get_open_url(self):
        return reverse('issues:issue_open', args=[self.project.pk, self.pk])

    class Meta:
        ordering = ['-index']


class Event(models.Model):
    """
    Any event on the timeline of an issue.
    """
    issue = models.ForeignKey('Issue')

    create_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey('auth.User')


class State(Event):
    """
    An open/close change.
    """
    closed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(State, self).save(*args, **kwargs)

        # update the cache state of the related issue.
        # save after saving this issue.
        self.issue.closed = self.closed

        try:
            self.issue.save()
        except:
            self.delete()
