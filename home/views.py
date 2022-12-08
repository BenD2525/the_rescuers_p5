from django.shortcuts import redirect, render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Reviews, Resident
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
            "id": review.id,
        })

    context = {
        "reviews": serialized_reviews
        }
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
        return render(request, 'home/add_review.html', context)
    
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
    template_name = 'home/delete_review.html'
    success_url = reverse_lazy('home:reviews')


class EditReview(UpdateView):
    '''View which allows the user to edit the selected review.'''
    model = Reviews
    template_name = 'home/edit_review.html'
    fields = ['title', 'content']


def residents(request):
    ''' Returns the featured residents page.'''

    serialized_residents = []

    residents = Resident.objects.all()

    for resident in residents:
        serialized_residents.append({
            "name": resident.name,
            "description": resident.description,
            "age": resident.age,
            "favourite_toy": resident.favourite_toy,
            "image_url": resident.image_url,
        })

    context = {
        "residents": serialized_residents
        }
    return render(request, 'home/featured_residents.html', context)
