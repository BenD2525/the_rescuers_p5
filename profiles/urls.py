from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit/<slug:slug>', views.EditProfile.as_view(), name='edit_profile'),
]