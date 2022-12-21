from django.shortcuts import render
from django.http import JsonResponse

def bag(request):
    ''' Returns the bag page.'''
    return render(request, 'bag/bag.html')


def update_bag(request):
    return JsonResponse("Item was added.", safe=False)

