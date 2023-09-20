from django.urls import path
from . import views

urlpatterns = [
    path('payments', views.payments),
    path('settings', views.settings),
    path('createcompany', views.createcompany),
    path('companies', views.joinGroup),
    path('logout', views.logout),
    path('dashboard', views.profile),
    ] 