from django.contrib import admin
from issues.models import *


admin.site.register(Issue)
admin.site.register(Event)
admin.site.register(State)
admin.site.register(Pin)
