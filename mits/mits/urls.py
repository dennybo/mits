from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^auth/', include('django.contrib.auth.urls')),

    url(r'^(?P<project_pk>\d+)/i/', include('issues.urls', namespace='issues')),
    url(r'^(?P<project_pk>\d+)/t/', include('tags.urls', namespace='tags')),
    url(r'^(?P<project_pk>\d+)/c/', include('checklists.urls', namespace='checklists')),

    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^', include('projects.urls', namespace='projects')),
]
