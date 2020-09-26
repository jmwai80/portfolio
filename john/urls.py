from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import contactView, successView


app_name = 'john'
urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
