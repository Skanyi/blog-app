from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)

class Email(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
