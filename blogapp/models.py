from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User,related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
