from django.conf.urls import url
import views

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
]
