from django.urls import path
from . import views


app_name = 'bag'

urlpatterns = [
    path('', views.bag, name='bag'),
    path('update_bag', views.update_bag, name='update_bag'),
]
