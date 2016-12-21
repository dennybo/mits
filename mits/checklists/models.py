from django.db import models
from django.urls import reverse


class Checklist(models.Model):
    project = models.ForeignKey('projects.Project')

    name = models.CharField(max_length=256)

    description = models.TextField(blank=True)

    issues = models.ManyToManyField('issues.Issue', blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('checklists:checklist_detail', args=[self.project.pk, self.pk])

    def get_update_url(self):
        return reverse('checklists:checklist_update', args=[self.project.pk, self.pk])

    def get_delete_url(self):
        return reverse('checklists:checklist_delete', args=[self.project.pk, self.pk])

    def get_add_issue_url(self):
        return reverse('checklists:checklist_add_issue', args=[self.project.pk, self.pk])

    def get_percentage(self):
        completed = self.issues.filter(closed=True).count()
        total = self.issues.count()

        if total == 0:
            return 0
        return completed * 100 / total
