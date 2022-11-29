from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
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


class DeleteReview(DeleteView):
    '''View which allows the user to delete the selected review.'''
    model = Reviews
    template_name = 'delete_review.html'
    success_url = reverse_lazy('reviews')


class EditReview(UpdateView):
    '''View which allows the user to edit the selected review.'''
    model = Reviews
    template_name = 'edit_review.html'
    fields = ['title', 'content']