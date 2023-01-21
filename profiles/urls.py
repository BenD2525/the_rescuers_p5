from django.urls import path
from . import views


app_name = 'profiles'
handler404 = 'home.views.custom_404'

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit/<slug:slug>', views.EditProfile.as_view(), name='edit_profile'),
    path('order/<int:pk>', views.order_detail, name='order_detail'),
]