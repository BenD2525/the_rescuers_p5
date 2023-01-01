from django.shortcuts import render
from products.models import Product


def checkout(request):
    ''' Returns the checkout page.'''
    return render(request, 'checkout/checkout.html')
