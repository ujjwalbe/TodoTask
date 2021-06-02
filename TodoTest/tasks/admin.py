from django.contrib import admin
from TodoTest.tasks.models import Project, Task, Tags 
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Tags)