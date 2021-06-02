from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from TodoTest.tasks.models import Project, Task, Tags
# Create your views here.


class HomeView(View):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        project = Project.objects.all()
        tasks = Task.objects.all()
        context ={
            'projects': project,
            'tasks': tasks
        }
        return render(request, self.template_name, context=context)


class AboutView(TemplateView):
    template_name = "pages/about.html"


