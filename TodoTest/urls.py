"""TodoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from TodoTest.tasks.api import urls as task_api_urls
from TodoTest.tasks.web import urls as task_web_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/v1/', include('rest_framework.urls')),
    path('api/v1/task/', include(task_api_urls), name='task_api'),
    path('task/', include('TodoTest.tasks.web.urls', namespace='task_web'))
]
