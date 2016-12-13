from django.contrib import admin
from models import *


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'is_administrator']


admin.site.register(Project)
admin.site.register(Membership, MembershipAdmin)
