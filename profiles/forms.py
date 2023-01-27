from django import forms
from checkout.models import Order
from .models import UserProfile


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


class UserProfileForm(forms.ModelForm):
    """
        Form which allows the user to update their profile details when
        placing an order.
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'slug', 'default_country',)
        widgets = {
            'default_first_name': forms.TextInput(attrs={'readonly': True}),
            'default_last_name': forms.TextInput(attrs={'readonly': True}),
            'default_email': forms.TextInput(attrs={'readonly': True}),
            'default_phone_number': forms.TextInput(attrs={'readonly': True}),
            'default_street_address_1': forms.TextInput(attrs={'readonly': True}),
            'default_street_address_2': forms.TextInput(attrs={'readonly': True}),
            'default_city': forms.TextInput(attrs={'readonly': True}),
            'default_postcode': forms.TextInput(attrs={'readonly': True}),
            'default_county': forms.TextInput(attrs={'readonly': True}),
        }
        labels = {
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_street_address_1': 'Address 1',
            'default_street_address_2': 'Address 2',
            'default_city': 'City',
            'default_postcode': 'Postcode',
            'default_county': 'County',
        }
