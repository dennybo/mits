from django.contrib import admin
from projects.models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'issue_index']


admin.site.register(Project, ProjectAdmin)
