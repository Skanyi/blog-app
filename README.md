
A simple django application that uses celery to schedule tasks. 

What remains right now:

Use rabbitmq as message broker and redis as backend result handler

# This is what is used to for transmitting the messages
Configure message broker - rabbitmq

# this is the database that will store the results of the worker
ResultBackend
Result backend to use for keeping task states and results.
Configure the results backend - not sure to either use django orm or redis. used redis

# create tasks. 
Create a send email task that is schedule to run after every 24 hours. 


<!-- Start the celery worker to monitor what is happening. On production you want to start the worker on the bg 
for development and testing it is okay-->
Test that the Celery worker is ready to receive tasks:
```celery -A blogsite worker -l info```

Test Celery task scheduler is ready for action:
```celery -A blogsite beat -l info```

<!-- start the rabittmq server -->
Am on Mac Os, 
```brew services rabbitmq start```

# after this works I will try to do the same on ubuntu server

<!-- Create a task that sends email after every 24 hours -->
what do i want to accomplish here. 
#overview
simply send an email to a specific email from a specific sender 
send an email to user with a specific email. 

# how to do it:
Have an email functions that send the email, it has the email message crafted already.

Use the task schedular to decide when the email is sent. 

<!-- what to do next: take a step back and look at what is happening and understand how the tasks are executed and then write the taks
This will ensure i understand the flow logic and can debug why a task was not executed at set time -->

resources:
https://github.com/celery/celery/blob/master/examples/django/proj/settings.py
https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#beat-custom-schedulers
https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
https://www.codementor.io/ankurrathore/asynchronous-task-with-rabbitmq-celery-and-django-8904ceway

https://code.tutsplus.com/tutorials/using-celery-with-django-for-background-task-processing--cms-28732