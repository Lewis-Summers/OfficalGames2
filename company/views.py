from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from company.models import *
from user.views import userAuth

def home(request, companyid):
    return render(request, "company/companybase.html")

def officials(request, companyid):
    # this should return a list of all the officals 
    return HttpResponse('hi')

def official(request, companyid, id):
    # this returns a single officals profile
    return

def leagues(request, companyid):
    # returns a list of leagues
    return

def league(request, companyid, id):
    # returns information about a league
    return

def complexs(request, companyid):
    # returns a list of complexs
    return HttpResponse(companyid)

def complex(request, companyid, complexid):
    # returns information about a complex including all the feilds
    return

def feild(request, companyid, complexid, feildid):
    # returns information about a feild in a complex
    return

def game(request, companyid, gameid):
    # returns information about a specific game
    return

def userdash(request):
    # returns user dash and all the important inforamtion like notifactions, profile, settings, upcoming games, and maybe some upcoming game information
    return

def mygames(request):
    if not userAuth(request):
        return HttpResponse("your not signed in")
    games = []
    user_assignments = Assignment.objects.select_related('game__sport', 'game__field', 'game__league', 'game__home_team', 'game__away_team').filter(user=user)
    user_assignments = user_assignments.prefetch_related('game__assignment_set__user').filter(user=request.user)
    for assignment in user_assignments:
        game = assignment.game
        sport = game.sport
        field = game.field
        league = game.league
        home_team = game.home_team
        away_team = game.away_team
        # Access other game details as needed

        # Access referees assigned to the same game efficiently
        referees = assignment.game.assignment_set.all()

        # for referee in referees:
        #     refassignment = user_assignments.prefetch_related('game__assignment_set__user').filter(user=referee)
        #     for assignment in refassignment:
        #         assignment.role
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