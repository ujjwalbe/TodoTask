from django.urls import path, re_path, include
from rest_framework import routers
from TodoTest.tasks.api import views

app_name='task_api'

router = routers.DefaultRouter()

router.register('tasks', views.GetAllTaskList, basename='task')
router.register('project', views.GetAllProjectList, basename='project')

urlpatterns=[
    re_path(r'', include(router.urls), name='tasks'),
    path('get/<str:id>', views.GetTaskView.as_view(), name='get'),
    path('get/project/<str:id>', views.GetProjectTaskView.as_view(), name='get'),
    path('asana/task/<str:id>', views.UpdateAsanaTask.as_view(), name='asana'),
]