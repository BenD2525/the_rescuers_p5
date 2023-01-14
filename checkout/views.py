from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:products_list'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    success_url = 'https://8000-bend2525-therescuersp5-77ck14x21o2.ws-eu82.gitpod.io/checkout/thankyou'
    context = {
        'order_form': order_form,
        'success_url': success_url
    }
    print(success_url)

    return render(request, template, context)


def order_success(request):
    """
    View that displays the successful order page after an order has been
    processed.
    """

    return render(request, 'checkout/thank_you.html')
