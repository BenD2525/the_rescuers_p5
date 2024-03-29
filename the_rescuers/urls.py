from django.contrib import admin
from django.urls import path, include

handler404 = 'home.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
