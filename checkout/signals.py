from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderDetail

@receiver(post_save, sender=OrderDetail)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when an order is updated or created.
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderDetail)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total when an order is deleted.
    """
    instance.order.update_total()