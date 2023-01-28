from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order, OrderDetail
from checkout.forms import OrderForm
from .forms import ShippingDetailForm, UserProfileForm


def user_profile(request):
    """ Checks whether the user is logged in, then displays the relevant
    profile or redirects to 404. Past orders from the user are displayed. """
    # If user is not logged in, display custom 404 page
    valid_user = request.user.is_authenticated
    if valid_user is False:
        return render(request, "404.html")

    profile = UserProfile.objects.get(user=request.user)
    template = 'profiles/user_profile.html'
    serialized_orders = []

    user_orders = Order.objects.filter(user=request.user)

    for order in user_orders:
        serialized_orders.append({
            "order_number": order.order_number,
            "order_total": order.order_total,
            "date": order.date,
            "id": order.id,
        })
    form = UserProfileForm(instance=profile)

    context = {
        "form": form,
        "orders": serialized_orders,
    }

    return render(request, template, context)


class EditProfile(UpdateView):
    '''View which allows the user to edit their profile details.'''
    model = UserProfile
    template_name = 'profiles/edit_profile.html'
    fields = ['default_first_name', 'default_last_name', 'default_email',
              'default_phone_number',
              'default_street_address_1', 'default_street_address_2',
              'default_city', 'default_postcode', 'default_county',
              'default_country']

    def get_object(self, queryset=None):
        """
        Retrieves the correct UserProfile object based on the slug variable
        passed in the URL.
        """
        return UserProfile.objects.get(user__username=self.kwargs['slug'])

    def form_valid(self, form):
        '''Displays message on successful editing of the profile.'''
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)


def order_detail(request, pk):
    '''View for the Order Detail page.
    Displays the selected Order from the Order model.'''
    valid_user = request.user.is_authenticated
    if valid_user is False:
        return render(request, "404.html")

    order = get_object_or_404(Order, pk=pk)
    order_products = OrderDetail.objects.filter(order=order)
    form = ShippingDetailForm(instance=order)
    order_total = order.order_total

    context = {
            "order_details_form": form,
            "order_products": order_products,
            "order_total": order_total,
        }

    return render(request, 'profiles/order_detail.html', context)
