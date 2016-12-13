from django.db import models


class Project(models.Model):
    # name for the project.
    name = models.CharField(max_length=64)

    members = models.ManyToManyField('auth.User', through='Membership')

    def __unicode__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    is_administrator = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
