from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from company.models import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request, companyid):
    # TODO this needs alot of error handling 
    compobj = Company.objects.get(id=companyid)
    employment = CompanyMembership.objects.get(user = request.user, company=compobj)
    print(employment.isAdmin)
    return render(request, "company/companybase2.html", {'employment': employment})
@login_required
def officials(request, companyid):
    # this should return a list of all the officals 
    return HttpResponse('hi')
@login_required
def official(request, companyid, id):
    # this returns a single officals profile
    return
@login_required
def leagues(request, companyid):
    # returns a list of leagues
    return
@login_required
def league(request, companyid, id):
    # returns information about a league
    return
@login_required
def complexs(request, companyid):
    # returns a list of complexs
    return HttpResponse(companyid)
@login_required
def complex(request, companyid, complexid):
    # returns information about a complex including all the feilds
    return
@login_required
def feild(request, companyid, complexid, feildid):
    # returns information about a feild in a complex
    return
@login_required
def game(request, companyid, gameid):
    # returns information about a specific game
    return
@login_required
def userdash(request, companyid):
    # returns user dash and all the important inforamtion like notifactions, profile, settings, upcoming games, and maybe some upcoming game information
    return HttpResponse(request, "userdash")
@login_required
def mygames(request):
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
@login_required

def selfassign(request, companyid):
    # returns information about open games and lets a user submit a request
    # FORM
    return

@login_required
def aftergames(request, companyid):
    # returns a list of all the games you need to do do after games on
    return

@login_required
def aftergame(request, companyid):
    # returns information to fill in for each game specifically should have easy switching between games
    # FORM
    return

@login_required
def estpay(request, companyid):
    # return a table with all the games and there value
    return

@login_required
def payscales(request, companyid):
    # return a table with all the games and there value
    return

@login_required
def gamepay(request, companyid):
    # return a table with all the games and there value
    return
