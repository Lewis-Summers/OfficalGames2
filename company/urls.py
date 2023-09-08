from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    
    #info
    path('info/officials',  views.officials, name='officials'),
    path('info/officials/official/<int:id>',  views.official, name='offical'),
    path('info/leagues',  views.leagues, name='leagues'),
    path('info/leagues/league/<int:id>',  views.league, name='league'),
    path('info/complexs', views.complexs, name='complex'),
    path('info/complexs/complex/<int:complexid>', views.complex, name='complex'),
    path('info/complexs/complex/<int:complexid>/feild/<int:feildid>', views.feild, name='feild'),
    path('info/game/<int:gameid>', views.game, name="game"), # this is right we wont have a all games page we just have a game look up type thing here

    # user dash
    path('userdash/', views.userdash),
    path('userdash/estpay', views.userdash),
    path('userdash/games/mygames', views.mygames),
    path('userdash/games/selfassign', views.selfassign),
    path('userdash/games/aftergames', views.aftergames),
    path('userdash/games/aftergame/<int:gameid>', views.aftergame),
]