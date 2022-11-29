from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Reviews
from .forms import ReviewForm


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


class AddReview(View):
    '''View which allows the user to add a new review.'''

    def get(self, request, *args, **kwargs):

        review = Reviews
        review_form = ReviewForm
             
        context = {
            'review': review,
            'review_form': review_form,
            'user': review.user,
            'title': review.title,
            'content': review.content,
        }
        return render(request, 'add_review.html', context)
    
    def post(self, request, *args, **kwargs):

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            obj = review_form.save(commit=False)
            obj.user = request.user
            obj.save()
            
        return redirect("home:reviews")


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
