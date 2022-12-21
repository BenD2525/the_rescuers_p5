from django.urls import path
from . import views


app_name = 'bag'

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
