from django import forms
from checkout.models import Order


class ShippingDetailForm(forms.ModelForm):
    """
        Form which displays the order detail for the chosen order.
    """
    class Meta:
        model = Order
        fields = ['order_total', 'first_name',
                  'last_name', 'email', 'phone_number', 'street_address_1',
                  'street_address_2', 'city', 'postcode', 'county', 'country']
        widgets = {
            'order_total': forms.TextInput(attrs={'readonly': True}),
            'first_name': forms.TextInput(attrs={'readonly': True}),
            'last_name': forms.TextInput(attrs={'readonly': True}),
            'email': forms.TextInput(attrs={'readonly': True}),
            'phone_number': forms.TextInput(attrs={'readonly': True}),
            'street_address_1': forms.TextInput(attrs={'readonly': True}),
            'street_address_2': forms.TextInput(attrs={'readonly': True}),
            'city': forms.TextInput(attrs={'readonly': True}),
            'postcode': forms.TextInput(attrs={'readonly': True}),
            'county': forms.TextInput(attrs={'readonly': True}),
            'country': forms.TextInput(attrs={'readonly': True}),
        }
