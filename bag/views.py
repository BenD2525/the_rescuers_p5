from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from django.contrib import messages


def bag(request):
    ''' Returns the bag page.'''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adds a quantity of a product to the shopping bag. """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    messages.success(request, "Item added to bag!")
    return redirect(redirect_url)


def amend_bag(request, item_id):
    """ Amends the quantity of an object in the bag. """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['bag'] = bag
    messages.success(request, "Bag updated.")
    return redirect(reverse('bag:bag'))


def remove_bag(request, item_id):
    """ Removes the object in the bag. """

    try:
        bag = request.session.get('bag', {})
        item = bag[item_id]
        bag.pop(item_id)

        request.session['bag'] = bag
        messages.warning(request, "Removed from bag.")
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
