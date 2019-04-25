from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/lessee', UserRegistrationFormView.as_view(), name='register_lessee'),
    path('register/renter', UserRegistrationFormView.as_view(), name='register_renter'),
    path('login/', UserLoginFormView.as_view(), name='login'),
    path('<int:pk>/profile', ProfileFormView.as_view(), name='profile'),
    path('logout/', UserLogoutVIew.as_view(), name='logout'),

]
