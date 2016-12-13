from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^issues/', include('issues.urls', namespace='issues')),
    url(r'^', include('projects.urls', namespace='projects')),
]
