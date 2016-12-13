from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        views.IssueDetailView.as_view(),
        name='issue_detail'
    ),

    url(
        r'^(?P<project_pk>\d+)/create/$',
        views.IssueCreateView.as_view(),
        name='issue_create'
    ),

    url(
        r'^update/(?P<pk>\d+)/$',
        views.IssueUpdateView.as_view(),
        name='issue_update'
    ),
]
