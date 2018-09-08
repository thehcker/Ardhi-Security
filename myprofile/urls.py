from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='account_login'),
    path('signup/', views.signup, name='account_signup'),
    path('logout/', views.logout, name='account_logout'),
    #path('prof/', views.userProfile, name='prof'),
    path('titledeed/', views.titleDeed, name='titledeed'),
    path('deed/', views.Deed, name='deed'),
    path('title/', views.title, name='title'),
    path('index/', views.index, name='index'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)