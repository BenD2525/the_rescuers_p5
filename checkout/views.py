import json

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from products.models import Product
from django.views.decorators.http import require_POST
from .models import Order, OrderDetail
from django.core.mail import send_mail
from the_rescuers.settings import DEFAULT_FROM_EMAIL
from templated_email import send_templated_mail
from django.contrib.auth.models import User

from .forms import OrderForm


def checkout(request):
    # Redirect to products if nothing in bag
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:products_list'))
    # Redirect to login/signup if user not logged in
    if not request.user.is_authenticated:
        messages.error(request, "Please login or create an account to continue with your purchase.")
        return redirect(reverse('account_login'))
    order_form = OrderForm()
    bag_products = []
    for item_id, quantity in bag.items():
        product = Product.objects.get(pk=item_id)
        name = product.name
        id = product.id
        bag_products.append({'name': name, 'id': id, 'quantity': quantity})
    bag_products = json.dumps(bag_products)
    # Attempt to prefill the form with any info the user maintains in
    # their profile
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
    success_url = reverse('checkout:order_success')
    thank_you = reverse('checkout:thank_you')
    context = {
        'order_form': order_form,
        'success_url': success_url,
        'bag_products': bag_products,
        'thank_you': thank_you,
    }
    return render(request, template, context)


def order_success(request):
    """
    View that creates a new object with the JSON data, then redirects to the
    thankyou page.
    """
    try:
        # Take the request, decode it, split it into bag_contents and
        # order_data and use this data to create a new order
        request2 = request.body
        my_json = request2.decode('utf8').replace("'", '"')
        json_data = json.loads(my_json)
        bag_contents = json_data.get('bagContents')
        bag_contents = json.loads(bag_contents)
        order_data = json_data.get('jsonData')
        order_data = json.loads(order_data)
        # Manually fill the user_id field with the user's id
        order_data["user_id"] = request.user.id
        # Remove the csrf token from the data
        order_data.pop("csrfmiddlewaretoken", None)
        # Create a new instance of the Order model using the order_data
        # received
        order = Order.objects.create(**order_data)
        order.save()
        # Loop through the bag_contents and save the details in OrderDetail
        # model
        for item in bag_contents:
            product = Product.objects.get(pk=item['id'])
            order_detail = OrderDetail(order=order, product=product,
                                       quantity=item['quantity'])
            order_detail.save()
        order.update_total()
        # Send email to the provided email address
        send_templated_mail(
            template_name='order_confirmation',
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[order.email],
            context={'name': order.first_name,
                     'order_number': order.order_number,
                     'order_total': order.order_total,
                     },
        )
        messages.success(request, "Thank you for your order!")
        return redirect(reverse('checkout:thank_you'))
    except Exception as e:
        return redirect(reverse('checkout:payment_failed'))


def thank_you(request):
    """
    View that displays the thankyou page after processing an order.
    """
    # Redirect to the custom 404 page if trying to access the page without
    # making an order
    valid_user = request.user.is_authenticated
    if valid_user is False:
        return render(request, "404.html")
    # Clear the bag now that the order has been
    # created
    request.session.pop('bag', None)
    messages.success(request, "Thankyou for your order!")
    return render(request, 'checkout/thank_you.html')


def payment_failed(request):
    """
    View that displays the cancelled payment page after an order has
    been cancelled.
    """
    valid_user = request.user.is_authenticated
    if valid_user is False:
        return render(request, "404.html")
    messages.error(request, "There was an error with your payment, please contact your bank.")
    return render(request, 'checkout/payment_failed.html')
