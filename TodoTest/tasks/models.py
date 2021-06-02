from django.db import models
import uuid
from django.db.models.signals import post_save, pre_save
from TodoTest.tasks.utils import asana_task
import datetime

# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=255)


class Project(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, null=False, blank=False
    )
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    description = models.CharField(null=True, blank=True, max_length=255)
    asana_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    TASK_CHOICE = (
        ("active", "active"),
        ("completed", "completed"),
        ("upcoming", "upcoming"),
    )
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, null=False, blank=False
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=False, blank=False, related_name="tasks"
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(choices=TASK_CHOICE, default="active", max_length=50)
    created = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1000)
    target = models.DateTimeField(blank=True, null=True)
    asana_task_id = models.CharField(max_length=255, blank=True, null=True)
    is_synced = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ForeignKey(
        Tags, on_delete=models.SET_NULL, null=True, blank=True, related_name="tags"
    )


    def __str__(self):
        return self.name

def task_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    Sync with asana
    """
    if created:
        asana_task.create_task(
            "pending",
            False,
            str(datetime.datetime.now()),
            False,
            instance.name,
            instance.description,
            [instance.project.asana_id],
            str(datetime.datetime.now()),
            task_id=instance.id,
            model=instance
        )
        instance.is_synced=True
        instance.save()


post_save.connect(task_post_save_receiver, sender=Task)


def project_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    Sync with asana
    """
    if created:
        asana_task.create_project(instance.name, instance.description, instance)


post_save.connect(project_post_save_receiver, sender=Project)
