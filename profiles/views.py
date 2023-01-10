from django.shortcuts import render
from .models import UserProfile


def user_profile(request):
    """ Displays the user's profile. """
    profile = UserProfile.objects.get(user=request.user)
    print(profile)
    template = 'profiles/user_profile.html'
    context = {
        'city': profile.default_city,
        'email': profile.default_email,
        'phone_number': profile.default_phone_number,
        'address_1': profile.default_street_address_1,
        'address_2': profile.default_street_address_2,
        'postcode': profile.default_postcode,
        'county': profile.default_county,
        'country': profile.default_country,

    }

    return render(request, template, context)