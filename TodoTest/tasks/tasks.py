from celery.schedules import crontab
from celery.utils.log import get_task_logger
from celery import Celery
import requests

from TodoTest.tasks.utils import asana_task

app = Celery()
logger = get_task_logger(__name__)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, task_save.s(), expires=10)


@app.task
def task_save():
    """
    Saves latest image from Flickr
    """
    asana_task.create_task("pending",  False,  str(datetime.datetime.now()), False, "some title", "description", ["1200402570959540"], str(datetime.datetime.now()))

    logger.info("Saved image from Flickr")


@app.task
def get_asana_task(project_id, asana_id):
    asana_task.update(project_id, asana_id)
    logger.info("Updated task")    

    