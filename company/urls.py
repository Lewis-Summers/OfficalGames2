from django.urls import path
from . import views

urlpatterns = [
    path('<int:companyid>/home', views.home, name='dashboard'),
    
    #info
    path('<int:companyid>/info/officials',  views.officials, name='officials'),
    path('<int:companyid>/info/officials/official/<int:id>',  views.official, name='offical'),
    path('<int:companyid>/info/leagues',  views.leagues, name='leagues'),
    path('<int:companyid>/info/leagues/league/<int:id>',  views.league, name='league'),
    path('<int:companyid>/info/complexs', views.complexs, name='complex'),
    path('<int:companyid>/info/complexs/complex/<int:complexid>', views.complex, name='complex'),
    path('<int:companyid>/info/complexs/complex/<int:complexid>/feild/<int:feildid>', views.feild, name='feild'),
    path('<int:companyid>/info/game/<int:gameid>', views.game, name="game"), # this is right we wont have a all games page we just have a game look up type thing here
    path('<int:companyid>/info/gamepay', views.payscales, name="gamepay"),
    path('<int:companyid>/info/gamepay/<int:scaleid>', views.gamepay, name="gamepay"), 

    # user dash
    path('<int:companyid>/userdash/', views.userdash),
    path('<int:companyid>/userdash/estpay', views.userdash),
    path('<int:companyid>/userdash/games/mygames', views.mygames),
    path('<int:companyid>/userdash/games/selfassign', views.selfassign),
    path('<int:companyid>/userdash/games/aftergames', views.aftergames),
    path('<int:companyid>/userdash/games/aftergame/<int:gameid>', views.aftergame),

    # admin
    # settings
    # payments 
    # create payscale
    # officials
    # send emails
    # announcements
    # path('settings')
]