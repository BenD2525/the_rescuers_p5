from django.urls import path
from . import views


app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('thankyou', views.order_success, name='order_success'),
]
