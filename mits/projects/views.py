from django.views import generic
from models import *
from forms import *


class ProjectListView(generic.ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(membership__user=self.request.user)


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['membership'] = Membership.objects.get(project=self.object,
                                                       user=self.request.user)
        return context


class ProjectCreateView(generic.CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        response = super(ProjectCreateView, self).form_valid(form)

        membership = Membership(project=self.object, user=self.request.user, is_administrator=True)
        membership.save()

        return response


class ProjectUpdateView(generic.UpdateView):
    model = Project
    form_class = ProjectForm
