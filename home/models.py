from django.db import models
from django.contrib.auth.models import User


class Reviews(models.Model):
    '''Model which stores the website reviews.'''
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

