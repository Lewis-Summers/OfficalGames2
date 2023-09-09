from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about us', views.home, name='home'),
    path('pricing', views.home, name='home'),
    path('our product', views.home, name='home'),
    path('contact us', views.home, name='home'),
]