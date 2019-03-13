from django.urls import path
from index.views import Index, rentView 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('rent/',rentView,name='rent'),
    #path('hire/',HireView.as_view(),name='hire'),
    # path('rent2/',rentView2,name='rent2'),
    # path('rent3/',rentView3,name='rent3')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)