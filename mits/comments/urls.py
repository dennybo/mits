from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^(?P<issue_pk>\d+)/create/$',
        views.CommentCreateView.as_view(),
        name='comment_create'
    ),

    url(
        r'^(?P<issue_pk>\d+)/update/(?P<pk>\d+)/$',
        views.CommentUpdateView.as_view(),
        name='comment_update'
    ),

    url(
        r'^(?P<issue_pk>\d+)/delete/(?P<pk>\d+)/$',
        views.CommentDeleteView.as_view(),
        name='comment_delete'
    ),
]
