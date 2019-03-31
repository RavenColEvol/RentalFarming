from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', UserRegistrationFormView.as_view(), name='register'),
    path('login/', UserLoginFormView.as_view(), name='login'),
    path('logout/', UserLogoutVIew.as_view(), name='logout'),

]
