from rest_framework import views
from rest_framework import viewsets, mixins, generics
from TodoTest.tasks.api import serializers
from TodoTest.tasks.models import Task, Project, Tags
from rest_framework.response import Response
from TodoTest.tasks import tasks
from TodoTest.tasks.utils import asana_task

class GetAllTaskList(viewsets.GenericViewSet, mixins.ListModelMixin):
    def get_serializer_class(self):
        if self.action == "list":
            return serializers.TaskSerializer
        return serializers.TaskSerializer

    def get_serializer_context(self):
        return {"request": self.request, "args": self.args, "kwargs": self.kwargs}

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset


class GetAllProjectList(viewsets.GenericViewSet, mixins.ListModelMixin):
    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ProjectSerializer
        return serializers.ProjectSerializer

    def get_serializer_context(self):
        return {"request": self.request, "args": self.args, "kwargs": self.kwargs}

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


class GetTaskView(views.APIView):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id', None)

        task_obj = Task.objects.get(id=task_id)
        task_json = serializers.TaskSerializer(task_obj).data
        return Response(task_json)


class GetProjectTaskView(views.APIView):

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('id', None)

        task_obj = Project.objects.get(id=project_id)
        task_json = serializers.ProjectSerializer(task_obj).data
        return Response(task_json)

class UpdateAsanaTask(views.APIView):

    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('id', None)
        project = Project.objects.get(id=project_id)
        asana_task.update(project.id,Project, Task, project.asana_id)
        # tasks.get_asana_task.apply_async((project.id, project.asana_id), retry=True)
        return Response('', status=200)
