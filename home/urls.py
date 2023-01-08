from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'home.views.custom_404'


app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews', views.reviews, name='reviews'),
    path('reviews/add', views.AddReview.as_view(), name='add_review'),
    path('reviews/delete/<int:pk>', views.DeleteReview.as_view(), name='delete_review'),
    path('reviews/edit/<int:pk>', views.EditReview.as_view(), name='edit_review'),
    path('residents', views.residents, name='residents'),
]
