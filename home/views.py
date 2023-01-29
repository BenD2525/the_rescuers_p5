from django.shortcuts import redirect, render, reverse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Reviews, Resident, Enquiry
from .forms import ReviewForm, EnquiryForm
from django.http import HttpResponse
from django.contrib import messages
from the_rescuers.settings import DEFAULT_FROM_EMAIL
from templated_email import send_templated_mail


def custom_404(request, exception):
    return render(request, '404.html', status=404)


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
        if not request.user.is_authenticated:
            messages.error(request, "Please login or create an account to add a review.")
            return redirect(reverse('account_login'))
        else:
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
            messages.success(request, "Thanks for adding a review!")
        return redirect("home:reviews")


class DeleteReview(DeleteView):
    '''View which allows the user to delete the selected review.'''
    model = Reviews
    template_name = 'home/delete_review.html'
    success_url = reverse_lazy('home:reviews')

    def delete(self, request, *args, **kwargs):
        '''Displays message on successful deletion of the review.'''
        messages.success(self.request, 'Your review was deleted successfully.')
        return super().delete(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        review = Reviews.objects.get(id=kwargs['pk'])
        if review.user != self.request.user:
            messages.warning(request, 'Please login or create an account to delete a review.')
            return redirect(reverse('account_login'))
        return super().dispatch(request, *args, **kwargs)


class EditReview(UpdateView):
    '''View which allows the user to edit the selected review.'''
    model = Reviews
    template_name = 'home/edit_review.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        '''Displays message on successful editing of the review.'''
        messages.success(self.request, 'Your review was updated successfully.')
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        review = Reviews.objects.get(id=kwargs['pk'])
        if review.user != self.request.user:
            messages.warning(request, 'Please login or create an account to edit a review.')
            return redirect(reverse('account_login'))
        return super().dispatch(request, *args, **kwargs)


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


class ContactUs(View):
    '''View which allows the user to contact the website.'''

    def get(self, request, *args, **kwargs):

        enquiry = Enquiry
        enquiry_form = EnquiryForm

        context = {
            'enquiry': enquiry,
            'enquiry_form': enquiry_form,
            'title': enquiry.title,
            'content': enquiry.content,
        }
        return render(request, 'home/contact_us.html', context)

    def post(self, request, *args, **kwargs):

        enquiry_form = EnquiryForm(data=request.POST)

        if enquiry_form.is_valid():
            obj = enquiry_form.save(commit=False)
            obj.save()
            send_templated_mail(
                template_name='contact_us',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[obj.email],
                context={'title': obj.title,
                         'content': obj.content,
                         },
            )
            messages.success(request, "Thanks for submitting an enquiry!")
        return redirect("home:home")
