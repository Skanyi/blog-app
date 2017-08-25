from __future__ import absolute_import
from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
import tempfile

logger = get_task_logger(__name__)

#  Since the app is loaded when django start, @task decorator is able to use it:
# The @shared_task decorator lets you create tasks without having any concrete app instance:

# @task(name="send_feedback_email_task")
# def send_feedback_email_task():
#     # sends a feedbak email every 24 hours
#     send_feedback_email()
#     logger.info("The feedback email was sent succesfully")

'''
Celery uses “celery beat” to schedule periodic tasks. 
Celery beat runs tasks at regular intervals, which are then executed by celery workers.
'''
# create a periodic task that will create a file daily at midnight
@periodic_task(
    run_every=(crontab(minute=0, hour=0)),
    name="create_file_task",
    ignore_result=True
)
# create a file in /tmp
def create_file_task():
    filename = tempfile.NamedTemporaryFile(delete=False)
    # write something on the file
    filename.write(b'My first trial to have the task running')
    print(filename.name)
    logger.info("The file  was created")

