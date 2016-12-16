from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=64)

    description = models.TextField()

    members = models.ManyToManyField('auth.User', through='Membership')

    # used to assign the last created issue index number.
    issue_index = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('projects:project_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('projects:project_delete', args=[self.pk])

    def get_membership(self, user):
        """
        Returns the current logged in user membership.
        :return:
        """
        try:
            return user.membership_set.filter(project=self).get()
        except:
            return None

    def get_members_update_url(self):
        return reverse('projects:project_members_update', args=[self.pk])


class Membership(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    is_administrator = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
