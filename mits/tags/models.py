from django.db import models
from django.urls import reverse

from colorful.fields import RGBColorField


class LowerCaseCharField(models.CharField):
    def to_python(self, value):
        return value.lower()


class Tag(models.Model):
    project = models.ForeignKey('projects.Project')

    name = LowerCaseCharField(max_length=64)

    color = RGBColorField()

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse('tags:tag_update', args=[self.project.pk, self.pk])

    def get_delete_url(self):
        return reverse('tags:tag_delete', args=[self.project.pk, self.pk])
