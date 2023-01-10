import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from django_countries.fields import CountryField
from profiles.models import UserProfile


class Order(models.Model):
    """
       Model for Orders, created when checking out the bag.
    """
    order_number = models.CharField(default='', max_length=32, null=False,
                                    editable=False)
    profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total each time a line item is added.
        """
        self.order_total = self.lineitems.aggregate(Sum('subtotal'))
        ['subtotal__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if there isn't one already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderDetail(models.Model):
    """
       Model for Order Detail, refers to the product model and details being
       checked out.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                   blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the save method and set the subtotal to the product price *
        quantity.
        """
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f' {self.product.name} | {self.order.order_number}'
