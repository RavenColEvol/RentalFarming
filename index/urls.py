from django.urls import path
from index.views import Index, RentView, HireView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('rent/',RentView.as_view(),name='rent'),
    path('hire/',HireView.as_view(),name='hire'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)