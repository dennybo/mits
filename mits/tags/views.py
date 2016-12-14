from django.urls import reverse
from django.views import generic

from models import *
from forms import *
from projects.mixins import *


class TagListView(ProjectMixin, ProjectAccessCheckMixin, generic.ListView):
    model = Tag

    def get_queryset(self):
        return self.get_project().tag_set.all()

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['active'] = 'tags'
        context['project'] = self.get_project()
        return context


class TagCreateView(ProjectMixin, ProjectAccessCheckMixin, generic.CreateView):
    model = Tag
    form_class = TagForm

    def form_valid(self, form):
        form.instance.project = self.get_project()
        return super(TagCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('tags:tag_list', args=[self.get_project().pk])


class TagUpdateView(ProjectMixin, ProjectAccessCheckMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm

    def get_success_url(self):
        return reverse('tags:tag_list', args=[self.get_project().pk])


class TagDeleteView(ProjectMixin, ProjectAccessCheckMixin, generic.DeleteView):
    model = Tag

    def get_success_url(self):
        return reverse('tags:tag_list', args=[self.get_project().pk])
