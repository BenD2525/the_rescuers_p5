from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'home'

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('', views.home, name='home'),
    path('reviews', views.reviews, name='reviews'),
    path('reviews/add', views.AddReview.as_view(), name='add_review'),
    path('reviews/delete/<int:pk>', views.DeleteReview.as_view(), name='delete_review'),
    path('reviews/edit/<int:pk>', views.EditReview.as_view(), name='edit_review'),
]
