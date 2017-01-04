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

    url(
        r'^report/(?P<pk>\d+)/$',
        views.ProjectReportView.as_view(),
        name='project_report'
    ),

    url(
        r'^members/(?P<pk>\d+)/$',
        views.ProjectMembershipUpdateView.as_view(),
        name='project_members_update'
    ),
]
