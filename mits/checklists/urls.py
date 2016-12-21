from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^$',
        views.ChecklistListView.as_view(),
        name='checklist_list'
    ),

    url(
        r'^(?P<pk>\d+)/$',
        views.ChecklistDetailView.as_view(),
        name='checklist_detail'
    ),

    url(
        r'^create/$',
        views.ChecklistCreateView.as_view(),
        name='checklist_create'
    ),

    url(
        r'^update/(?P<pk>\d+)/$',
        views.ChecklistUpdateView.as_view(),
        name='checklist_update'
    ),

    url(
        r'^delete/(?P<pk>\d+)/$',
        views.ChecklistDeleteView.as_view(),
        name='checklist_delete'
    ),

    url(
        r'^addissue/(?P<pk>\d+)/$',
        views.ChecklistAddIssueView.as_view(),
        name='checklist_add_issue'
    ),
]
