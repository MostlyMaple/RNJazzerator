from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"), 
    path('genPrimes/', views.genPrimes, name="genPrimes"), 
    path('piano/', views.piano, name="piano"), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)