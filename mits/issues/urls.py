from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^$',
        views.IssueListView.as_view(),
        name='issue_list'
    ),

    url(
        r'^closed/$',
        views.ClosedIssueListView.as_view(),
        name='issue_list_closed'
    ),

    url(
        r'^(?P<pk>\d+)/$',
        views.IssueDetailView.as_view(),
        name='issue_detail'
    ),

    url(
        r'^(?P<pk>\d+)/close/$',
        views.IssueCloseView.as_view(),
        name='issue_close'
    ),

    url(
        r'^(?P<pk>\d+)/open/$',
        views.IssueOpenView.as_view(),
        name='issue_open'
    ),

    url(
        r'^create/$',
        views.IssueCreateView.as_view(),
        name='issue_create'
    ),

    url(
        r'^update/(?P<pk>\d+)/$',
        views.IssueUpdateView.as_view(),
        name='issue_update'
    ),

    url(
        r'^(?P<pk>\d+)/tags/update/$',
        views.IssueTagsUpdateView.as_view(),
        name='issue_tags_update'
    ),
]
