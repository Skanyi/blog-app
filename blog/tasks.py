# create tasks here that send an email every 24 hours
# for testing purposes we will use every minute and when it works change to 24 hours

from __future__ import absolute_import
from celery import shared_task, task
from celery.utils.log import get_task_logger
from celery.schedules import crontab
import tempfile
from blogsite.celery import app
# from .emails import send_feedback_email
logger = get_task_logger(__name__)

app.conf.beat_schedule = {
    'create-file-every-single-minute': {
        'task': 'blog.tasks.create_file_task',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}

#  Since the app is loaded when django start, @shared_task decorator is able to use it:
# The @shared_task decorator lets you create tasks without having any concrete app instance:
# @shared_task(name="send_feedback_email_task")
# @app.task
# def send_feedback_email_task():
#     # sends a feedbak email every 24 hours
#     send_feedback_email()
#     logger.info("The feedback email was sent succesfully")
    
# create a file in /tmp
@app.task
def create_file_task():
    filename = tempfile.NamedTemporaryFile(delete=False)
    # write something on the file
    filename.write(b'My first trial to have the task running')
    print(filename.name)
    logger.info("The file  was created")

# create_file_task()


# @app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)