from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', UserRegistrationFormView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]
