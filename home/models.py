from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product


class Reviews(models.Model):
    '''Model which stores the website reviews.'''
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''Defines a redirect URL after editing/deleting.'''
        return reverse('home:reviews')


class Resident(models.Model):
    '''Model which stores the residents of the shelter.'''
    name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.IntegerField()
    favourite_toy = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

