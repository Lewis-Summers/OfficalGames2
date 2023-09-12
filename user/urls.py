from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login_view),
    path('user', views.profile),
    path('payments', views.payments),
    path('settings', views.settings),
    path('createcompany', views.createcompany),
    path('companies', views.joinGroup),
    ]