from django.shortcuts import render
from .models import UserProfile
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages


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
        'user': profile.user,
    }

    return render(request, template, context)


class EditProfile(UpdateView):
    '''View which allows the user to edit their profile details.'''
    model = UserProfile
    template_name = 'profiles/edit_profile.html'
    fields = ['default_email', 'default_phone_number',
              'default_street_address_1', 'default_street_address_2',
              'default_city', 'default_postcode', 'default_county',
              'default_country']

    def form_valid(self, form):
        '''Displays message on successful editing of the profile.'''
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)
