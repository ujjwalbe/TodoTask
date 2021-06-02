from rest_framework import serializers

from TodoTest.tasks.models import Project, Task, Tags


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Project
        fields = [
            'name',
            'asana_id',
            'is_active',
            'tasks',
            'created',
            'description',
        ]
