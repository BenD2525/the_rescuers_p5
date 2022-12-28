from django.urls import path
from . import views


app_name = 'bag'

urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('amend/<item_id>/', views.amend_bag, name='amend_bag'),
    path('remove/<item_id>/', views.remove_bag, name='remove_bag'),
]
