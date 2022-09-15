from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Post(models.Model):
    STATUS_CHOICE = (
        ('pub', 'publish'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
