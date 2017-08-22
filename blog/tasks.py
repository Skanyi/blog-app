# create tasks here that send an email every 24 hours
# for testing purposes we will use every minute and when it works change to 24 hours

from __future__ import absolute_import
from celery import shared_task, task
from celery.utils.log import get_task_logger
from celery.schedules import crontab

from blogsite.celery import app
from .emails import send_feedback_email

logger = get_task_logger(__name__)

app.conf.beat_schedule = {
    'send-email-every-single-minute': {
        'task': 'blog.tasks.send_feedback_email_task',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}

#  Since the app is loaded when django start, @shared_task decorator is able to use it:
# The @shared_task decorator lets you create tasks without having any concrete app instance:
# @shared_task(name="send_feedback_email_task")
@app.task
def send_feedback_email_task():
    # sends a feedbak email every 24 hours
    send_feedback_email()
    logger.info("The feedback email was sent succesfully")
    