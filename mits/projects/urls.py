from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^$',
        views.ProjectListView.as_view(),
        name='project_list'
    ),

    url(
        r'^(?P<pk>\d+)/$',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),

    url(
        r'^create/$',
        views.ProjectCreateView.as_view(),
        name='project_create'
    ),

    url(
        r'^update/(?P<pk>\d+)/$',
        views.ProjectUpdateView.as_view(),
        name='project_update'
    ),

    url(
        r'^delete/(?P<pk>\d+)/$',
        views.ProjectDeleteView.as_view(),
        name='project_delete'
    ),
]
