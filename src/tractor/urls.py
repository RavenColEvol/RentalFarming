from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (TractorDetailView,
                    MyTractorView,
                    TractorCreateView,
                    TractorUpdateView,
                    TractorDeleteView)

app_name = 'tractor'

urlpatterns = [
    path('', MyTractorView.as_view(), name='my_tractor'),
    path('<int:pk>/', TractorDetailView.as_view(), name='detail'),
    path('add/', TractorCreateView.as_view(), name='add'),
    path('<int:pk>/update', TractorUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', TractorDeleteView.as_view(), name='delete'),
    # path('checkout/', Checkout().as_view(), name='checkout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
