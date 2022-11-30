from django.shortcuts import redirect, render


def products(request):
    ''' Returns the home page.'''
    return render(request, 'products/products.html')

