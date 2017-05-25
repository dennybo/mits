from django.conf.urls import url
from tags import views

urlpatterns = [
    url(
        r'^$',
        views.TagListView.as_view(),
        name='tag_list'
    ),

    url(
        r'^create/$',
        views.TagCreateView.as_view(),
        name='tag_create'
    ),

    url(
        r'^update/(?P<pk>\d+)/$',
        views.TagUpdateView.as_view(),
        name='tag_update'
    ),

    url(
        r'^delete/(?P<pk>\d+)/$',
        views.TagDeleteView.as_view(),
        name='tag_delete'
    ),
]
