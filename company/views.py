from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from company.models import *
from django.contrib.auth.decorators import login_required
# from urllib.parse import urlparse, parse_qs
from django.apps import apps


def getemployment(request, companyid):
    # TODO this needs alot of error handling 
    compobj = Company.objects.get(id=companyid)
    return CompanyMembership.objects.get(user = request.user, company=compobj)


@login_required
def home(request, companyid):
    employment = getemployment(request, companyid)
    return render(request, "company/home.html", {'employment': employment})

@login_required
def officials(request, companyid): # DONE
    # this should return a list of all the officals 
    employment = getemployment(request, companyid)
    refs = CompanyMembership.objects.filter(company=companyid)
    return render(request, "company/officials.html", {'employment': employment, 'refs':refs})

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
def gameinfo(request, companyid, gameid):
    try:
        company = Company.objects.get(id=companyid)
    except:
        return # company does not exist
    
    try:
        game = Game.objects.get(id=gameid)
    except:
        return # not a valid game id
    payload = {
        "Game ID":game.assigned_game_id,
        "Sport":game.sport.name,
        "Age Group":game.age,
        "Gender":game.gender,
        "Field": None if game.field is None else f'{game.field.complex.name} - {game.field.name}',
        "League":game.league,
        "Home Team":game.home_team,
        "Away Team":game.away_team,
        "Date Time":game.date_time
    }
    
    if game.happened():
        payload['Home Score'] = (game.home_score)
        payload['Away Score'] = (game.away_score)
        payload['Game Report'] = (game.game_report)

    for det in payload:
        payload[det]= '--' if payload[det] is None else payload[det]

    print(payload)
    return render(request, "company/game.html", {"game": game, "payload": payload})

@login_required
def mygames(request): # not done
    games = []
    user_assignments = Assignment.objects.select_related('game__sport', 'game__field', 'game__league', 'game__home_team', 'game__away_team').filter(user=request.user)
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
    if request.method == 'POST':
        pass
    company = Company.objects.get(id = companyid)
    employment = getemployment(request, companyid)
    sports = Sport.objects.filter(company=company)
    games = []
    
    for sport in sports:
        games.append([{
        'id': game.id,
        "gameid": game.assigned_game_id,
        "sport": {'val': game.sport.name, 'id': game.sport.id },
        "age": {'val': game.age.title if game.age else '--' , 'id':game.age.id if game.age else '--' },
        "gender": game.gender if game.gender else '--',
        "complex": {'val': game.field.complex.name if game.field else '--', 'id': game.field.complex.id if game.field else '--'},
        "field": {'val': game.field.name if game.field else '--', 'id': game.field.id if game.field else '--'},
        "League": {'val': game.league.name if game.league else '--', 'id': game.league.id if game.league else '--'},
        "dateTime":game.date_time if game.date_time else '--'
    } for game in Game.objects.filter(sport=sport)])
        
    print(games)
    sportCriteriaData = [{
        'name': sport.name,
        "id": sport.id,
        'leagues': [{
            'name': league.name,
            'id': league.id,
        } for league in Leagues.objects.filter(sport=sport)],
        'ages': [{
            'name': age.title,
            'id': age.id
        } for age in Age.objects.filter(sport=sport)]
    } for sport in sports]

    complexCriteriaData = [{
        'name':complex.name,
        'id':complex.id,
        "feilds":[{
            "name": field.name,
            'id': field.id,
        }for field in Field.objects.filter(complex=complex)]
    } for complex in Complex.objects.filter(company=company)]


    return render(request, 'company/selfassign.html', {'employment': employment, 'sports': sports, 'complexCriteriaData':complexCriteriaData, 'sportCriteriaData': sportCriteriaData})

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


@login_required
def editgame(request, companyid, gameid):
    employment = getemployment(request, companyid)
    company = Company.objects.get(id=companyid)
    game = Game.objects.get(id=gameid)
    refs = CompanyMembership.objects.filter(company=company)
    sports = Sport.objects.filter(company=company)

    return render(request, "company/editgame.html", {'employment': employment, 'companyid': companyid, 'game': game, 'sports':sports})

@login_required
def games(request, companyid):#doneish
    employment = getemployment(request, companyid)
    sports = [sport.name for sport in Sport.objects.filter(company = Company.objects.get(id = companyid))]
    return render(request, "company/games.html", {'employment': employment, 'sports': sports, 'companyid': companyid})

#@login_required
def fetchgamesdata(request): #doneish
    selected_option = request.GET.get('selected_option')
    companyid2 = request.GET.get('companyid')

    selectedSport = Sport.objects.get(name=selected_option, company=Company.objects.get(id=companyid2))
    selectedGames = Game.objects.filter(sport=selectedSport)
    data = []

    games = Game.objects.filter(sport_id=selectedSport).values(
    'id',
    'assigned_game_id',
    'league__name',  # Assuming 'name' is a field in the 'Leagues' model
    'field__complex__name',  # Replace 'complex_field' with the actual field name in the 'Field' model
    'date_time',
    'field__name'  # Select the 'field' ForeignKey directly
    )


    # Iterate through the queryset and access the selected fields
    for game in games:    
        refs = Assignment.objects.filter(game=Game.objects.get(id=game['id']))
        refdata = []
        for ref in refs: # gets all data from the refs and puts it in a dictionary to be put into the gamedata dict
            ref_info = {
                'full_name': ref.user.get_full_name(),
                'role': ref.role.name
            }
            refdata.append(ref_info)
        print(refdata)
        gamedata = {
             'id':game['id'],
             'assid': game['assigned_game_id'],
             'league': game['league__name'],
             'complex': game['field__complex__name'],
             'datetime': game['date_time'],
             'field': game['field__name'],
             'refs': refdata
             }
        for feild in gamedata:
            gamedata[feild] = '--' if gamedata[feild] is None else gamedata[feild] # sets all null feilds to -- 
        data.append(gamedata)
    return JsonResponse(data, safe=False)

def fetchsportdata(request):# needs hella error handling
    companyid = request.GET.get('companyid')
    company = Company.objects.get(id=companyid)
    # if request.GET.get('case') == 'sport':
    #     sportid = request.GET.get('id')
    #     selectedSport = Sport.objects.get(id=selectedSport, Company=Company.objects.get(id=companyid))
    #     leagues = Leagues.objects.filter(sport=selectedSport)
    # elif request.GET.get('case') == 'else':
    #     laegueid = request.GET.get('id')
    #     league = Leagues.objects.get()
    sportid = request.GET.get('id')
    selectedSport = Sport.objects.get(id=sportid, company=company)
    leagues = Leagues.objects.filter(sport=selectedSport)
    
    leaguesList = []
    for league in leagues:
        teamsList = []
        teamsInLeague = Teams.objects.filter(league=league)
        for team in teamsInLeague:
            teamsList.append({'name':team.team_name, 'id': team.id})
        leaguesList.append({"name": league.name, 'id': league.id, 'teams': teamsList})
    ageList = [{'id': age.id, 'name': age.title} for age in Age.objects.filter(sport=selectedSport)]
    complexList = [{'id': complex.id, 'name': complex.name, 'feilds': [{'name': feild.name, 'id': feild.id} for feild in Field.objects.filter(complex=complex)]} for complex in Complex.objects.filter(company=company)]
    print(complexList)
    payload = {
        'leagues': leaguesList,
        "ages": ageList,
        'complexs': complexList
    }
    return JsonResponse(payload, safe=False)

def selfassignsubmit():
    pass