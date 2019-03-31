from django.urls import path
from index.views import Index, rentView, search, signIn

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('rent/',rentView,name='rent'),
    path('hire/',search,name='hire'),
    path('signin/',signIn,name='signIn')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)