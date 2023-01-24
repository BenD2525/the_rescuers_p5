from django.urls import path
from . import views


app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('thank_you', views.thank_you, name='thank_you'),
    path('order_success', views.order_success, name='order_success'),
    path('payment_failed', views.payment_failed, name='payment_failed'),
]
