from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    '''Form which allows the user to add a new review.'''
    class Meta:
        '''Class which specifies setup of the form.'''
        model = Reviews
        fields = ('title', 'content')
        labels = {'title': 'Title:', 'content': 'Add your review here:'}
