from django.db import models


class Project(models.Model):
    # name for the project.
    name = models.CharField(max_length=64)

    description = models.TextField()

    members = models.ManyToManyField('auth.User', through='Membership')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'projects:project_detail', [self.pk]

    @models.permalink
    def get_update_url(self):
        return 'projects:project_update', [self.pk]

    @models.permalink
    def get_delete_url(self):
        return 'projects:project_delete', [self.pk]


class Membership(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    is_administrator = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
