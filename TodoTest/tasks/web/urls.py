from django.urls import path, re_path, include
from TodoTest.tasks.web import views

app_name="task_web"

urlpatterns=[
    path('new', views.CreateNewTask.as_view(), name='new'),
    path('list-new', views.CreateNewProject.as_view(), name='new-list')

]