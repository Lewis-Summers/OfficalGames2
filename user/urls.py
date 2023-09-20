from django.urls import path
from . import views
from OfficalGames2 import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('payments', views.payments),
    path('settings', views.settings),
    path('createcompany', views.createcompany),
    path('companies', views.joinGroup),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('dashboard', views.profile),
    ] 