from django.shortcuts import render


def home(request):
    ''' Returns the home page.'''
    return render(request, 'home/index.html')


def reviews(request):
    ''' Returns the home page.'''
    return render(request, 'home/reviews.html')
