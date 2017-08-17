
A simple django application that uses celery to schedule tasks. 

What remains right now:

# This is what is used to for transmitting the messages
Configure message broker - rabbitmq

# this is the database that will store the results of the worker
ResultBackend
Result backend to use for keeping task states and results.
Configure the results backend - not sure to either use django orm or redis. 

# create tasks. 
Create a send email task that is schedule to run after every 24 hours. 


resources:
https://github.com/celery/celery/blob/master/examples/django/proj/settings.py
https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#beat-custom-schedulers
https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
https://www.codementor.io/ankurrathore/asynchronous-task-with-rabbitmq-celery-and-django-8904ceway