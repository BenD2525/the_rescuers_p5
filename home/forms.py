from django import forms
from .models import Reviews, Enquiry


class ReviewForm(forms.ModelForm):
    '''Form which allows the user to add a new review.'''
    class Meta:
        '''Class which specifies setup of the form.'''
        model = Reviews
        fields = ('title', 'content')
        labels = {'title': 'Title:', 'content': 'Add your review here:'}


class EnquiryForm(forms.ModelForm):
    '''Form which allows the user to submit an enquiry.'''
    class Meta:
        '''Class which specifies setup of the form.'''
        model = Enquiry
        fields = ('title', 'content', 'email')
        labels = {'title': 'Title:', 'content': 'Add your enquiry here:',
                  'email': 'Your email address'}
