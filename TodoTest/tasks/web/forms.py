from django import forms
from TodoTest.tasks.models import Task, Project

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'project',
            'name',
            'description',
            'assigned_to',
            'status'
        ]

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'name',
            'description'
        ]