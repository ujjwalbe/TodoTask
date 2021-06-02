from django import views, template
from django.shortcuts import render, redirect
from TodoTest.tasks.web.forms import TaskForm, ProjectForm
from django.urls import reverse, reverse_lazy
from TodoTest.tasks.models import Task, Project, Tags


class CreateNewTask(views.View):
    template_name = "tasks/task_new.html"

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        context = {"form": form, "projects": Project.objects.all()}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.project = Project.objects.all().first()
            task.save()
            return redirect(reverse_lazy("home"))
        return render(request, self.template_name, {"form": TaskForm()})


class CreateNewProject(views.View):
    template_name = "tasks/project_new.html"

    def get(self, request, *args, **kwargs):
        form = ProjectForm()
        context = {"form": form, "projects": Project.objects.all()}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("home"))
        return render(request, self.template_name, {"form": ProjectForm()})
