from django.views import generic
from models import *


class ProjectDetailView(generic.DetailView):
    model = Project
