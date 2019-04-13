from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import TractorDetailView, MyTractorView

app_name = 'tractor'

urlpatterns = [
    path('', MyTractorView.as_view(), name='my_tractor'),
    path('<int:pk>/', TractorDetailView.as_view(), name='detail'),
    path('add/', TractorDetailView.as_view(), name='detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
