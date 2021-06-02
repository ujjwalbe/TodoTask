import sys, os
import json
from six import print_
import datetime
import requests

ACCESS_TOKEN = "1/1200402569058608:24e5c4d2dbe0cb48433fadfd83d84c4e"


def create_task(
    status,
    completed,
    due_on,
    liked,
    title,
    description,
    project_list,
    start_on,
    task_id,
    model
):
    obj = {
        "data": {
            "approval_status": status,
            "completed": completed,
            "due_on": "2021-06-03 20:36:04.898888",
            "liked": liked,
            "name": title,
            "notes": description,
            "projects": project_list,
            "start_on": start_on,
            "tags": [],
            "workspace": "1200402500257305",
        }
    }
    endpoint = "https://app.asana.com/api/1.0/tasks"

    data = json.dumps(obj)
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    resp = requests.post(endpoint, data=data, headers=headers).json()
    astask_id = resp['data']['gid']
    print(astask_id)

    model.asana_task_id = str(astask_id)
    model.save()
    print(model, resp)


def create_project(name, description, project):
    obj = {
        "data": {
            "archived": False,
            "color": "light-green",
            "default_view": "calendar",
            "due_date": "2021-06-15",
            "html_notes": f"<body>{description}.</body>",
            "is_template": False,
            "name": name,
            "notes": f"{description}",
            "public": False,
            "start_on": "2021-06-03",
            "workspace": "1200402500257305",
        }
    }
    endpoint = "https://app.asana.com/api/1.0/projects"

    print(obj)
    data = json.dumps(obj)
    print(data)
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    resp = requests.post(endpoint, data=data, headers=headers).json()

    project.asana_id = resp['data']['gid']
    project.save()
    print(resp)


def update(project, project_obj, task_obj, asana_id ):
    asana_id = asana_id

    endpoint = f"https://app.asana.com/api/1.0/projects/{asana_id}/tasks"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    resp = requests.get(endpoint, headers=headers).json()
    asana_task = resp['data']
    project_inst = project_obj.objects.get(id=project)
    tasks = task_obj.objects.filter(project=project)
    print(tasks)
    add_task = []
    if len(tasks) > 0:
        for task in asana_task:
            for tsk in tasks:
                if tsk.asana_task_id != task['gid']:
                    add_task.append(task)
    elif len(asana_task) >0:
        for task in asana_task:
            add_task.append(task)
    print(add_task)
    if len(add_task) > 0:
        for task in add_task:
            print(task)
            obj = task_obj.objects.create(project=project_inst, name=task['name'], description=task['name'], asana_task_id=task['gid'], is_synced=True)
    print(resp)
