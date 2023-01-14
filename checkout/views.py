from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse
from profiles.models import UserProfile


from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:products_list'))
    order_form = OrderForm()
    # Attempt to prefill the form with any info the user maintains in
    # their profile
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order_form = OrderForm(initial={
            'first_name': profile.default_first_name,
            'last_name': profile.default_last_name,
            'email': profile.default_email,
            'phone_number': profile.default_phone_number,
            'country': profile.default_country,
            'postcode': profile.default_postcode,
            'city': profile.default_city,
            'street_address_1': profile.default_street_address_1,
            'street_address_2': profile.default_street_address_2,
            'county': profile.default_county,
        })
    template = 'checkout/checkout.html'
    success_url = 'https://8000-bend2525-therescuersp5-77ck14x21o2.ws-eu82.gitpod.io/checkout/thankyou'
    context = {
        'order_form': order_form,
        'success_url': success_url
    }
    return render(request, template, context)


def order_success(request):
    """
    View that displays the successful order page after an order has been
    processed.
    """
    # order_number

    # context = {
    #     'order_number': order_number,
    # }

    return render(request, 'checkout/thank_you.html', context)
