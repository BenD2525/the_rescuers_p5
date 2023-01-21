import json

from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from profiles.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.views.decorators.http import require_POST
from .models import Order, OrderDetail


from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products:products_list'))
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
    success_url = 'https://the-rescuers-p5.herokuapp.com/checkout/order_success'
    thank_you = 'https://the-rescuers-p5.herokuapp.com/checkout/thank_you'
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
    # Take the request, decode it, split it into bag_contents and order_data
    # and use this data to create a new order
    request2 = request.body
    my_json = request2.decode('utf8').replace("'", '"')
    json_data = json.loads(my_json)
    bag_contents = json_data.get('bagContents')
    bag_contents = json.loads(bag_contents)
    order_data = json_data.get('jsonData')
    order_data = json.loads(order_data)
    # Manually fill the user_id field with the user's id
    order_data["user_id"] = request.user.id
    # Create a new instance of the Order model using the order_data received
    order = Order.objects.create(**order_data)
    order.save()
    # Loop through the bag_contents and save the details in OrderDetail model
    for item in bag_contents:
        product = Product.objects.get(pk=item['id'])
        order_detail = OrderDetail(order=order, product=product, quantity=item['quantity'])
        order_detail.save()
    order.update_total()

    return


def thank_you(request):
    """
    View that displays the thankyou page after processing an order.
    """
    return render(request, 'checkout/thank_you.html')


@csrf_exempt
def payment_canceled(request):
    """
    View that displays the cancelled payment page after an order has been
    cancelled.
    """
    return render(request, 'checkout/payment_cancelled.html')
