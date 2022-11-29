from django.shortcuts import render
from .models import Reviews


def home(request):
    ''' Returns the home page.'''
    return render(request, 'home/index.html')


def reviews(request):
    ''' Returns the reviews page.'''

    serialized_reviews = []

    reviews = Reviews.objects.all()

    for review in reviews:
        serialized_reviews.append({
            "title": review.title,
            "content": review.content,
            "user": review.user,
            "created": review.created,
            "updated": review.updated,
        })

    context = {
        "reviews": serialized_reviews
        }
    print(serialized_reviews)
    return render(request, 'home/reviews.html', context)
