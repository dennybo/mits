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

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('issues:issue_detail', args=[self.project.pk, self.pk])

    def get_update_url(self):
        return reverse('issues:issue_update', args=[self.project.pk, self.pk])

    class Meta:
        ordering = ['-index']
