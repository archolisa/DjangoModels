from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    Title = models.CharField(max_length=200, unique=True)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now= True)
    

    class Meta:
        ordering = ['-Created_date']

    def __str__(self):
        return self.title
