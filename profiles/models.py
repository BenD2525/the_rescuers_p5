from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class UserProfile(models.Model):
    """
    A model which stores the user's profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    default_first_name = models.CharField(max_length=30, null=False,
                                          blank=True)
    default_last_name = models.CharField(max_length=30, null=False,
                                         blank=True)
    default_email = models.EmailField(max_length=250, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address_1 = models.CharField(max_length=80, null=True,
                                                blank=True)
    default_street_address_2 = models.CharField(max_length=80, null=True,
                                                blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label="Country *", null=True,
                                   blank=True)

    def __str__(self):
        """
        Sets a string of the model's name.
        """
        return self.user.username

    def save(self, *args, **kwargs):
        """
        Saves the model instance with a slug based on the user.
        """
        if not self.slug:
            self.slug = slugify(self.user)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        '''Defines a redirect URL after editing/deleting.'''
        return reverse('profiles:user_profile')


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile, depending on whether it exists or not.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
