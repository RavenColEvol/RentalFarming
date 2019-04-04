from django.urls import path
from index.views import index, rentView, search, signIn,checkout,tractor

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('rent/',rentView,name='rent'),
    path('hire/',search,name='hire'),
    path('signin/',signIn,name='signIn'),
    path('checkout/<int:tractor_id>',checkout,name='checkout'),
    path('rent/<int:tractor_id>/',tractor,name='tractor')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)