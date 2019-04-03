from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Index, rent_view, search_view, signin_view

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('rent/', rent_view, name='rent'),
    path('hire/', search_view, name='hire'),
    path('signin/', signin_view, name='signIn')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
