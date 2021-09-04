from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=600, null=False)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feed/feed.html')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

