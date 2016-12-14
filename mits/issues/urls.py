from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^$',
        views.IssueListView.as_view(),
        name='issue_list'
    ),

    url(
        r'^(?P<pk>\d+)/$',
        views.IssueDetailView.as_view(),
        name='issue_detail'
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
