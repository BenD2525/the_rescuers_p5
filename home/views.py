from django.shortcuts import render


def home(request):
    ''' Returns the home page.'''
    return render(request, 'home/index.html')
