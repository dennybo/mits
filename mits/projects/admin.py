from django.contrib import admin
from models import *


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'is_administrator']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'issue_index']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Membership, MembershipAdmin)
