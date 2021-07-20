from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('search/', views.search_category, name='search'),
    path('location/location/', views.image_location, name='location'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)