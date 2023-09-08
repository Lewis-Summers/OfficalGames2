from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request, "test.html")

def officials(request):
    # this should return a list of all the officals 
    return HttpResponse('hi')

def official(request, id):
    # this returns a single officals profile
    return

def leagues(request):
    # returns a list of leagues
    return

def league(request, id):
    # returns information about a league
    return

def complexs(request, complexid):
    # returns a list of complexs
    return

def complex(request, complexid):
    # returns information about a complex including all the feilds
    return

def feild(request, complexid, feildid):
    # returns information about a feild in a complex
    return

def game(request, gameid):
    # returns information about a specific game
    return

def userdash(request):
    # returns user dash and all the important inforamtion like notifactions, profile, settings, upcoming games, and maybe some upcoming game information
    return

def mygames(request):
    # returns information about my games by date ig
    return

def selfassign(request):
    # returns information about open games and lets a user submit a request
    # FORM
    return

def aftergames(request):
    # returns a list of all the games you need to do do after games on
    return

def aftergame(request):
    # returns information to fill in for each game specifically should have easy switching between games
    # FORM
    return

def estpay(request):
    # return a table with all the games and there value
    return