from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'products'

urlpatterns = [
    path('products', views.products, name='products'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
]
