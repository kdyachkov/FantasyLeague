import json
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Player, WeeklyPoints, Team, User


def index(request):

    #w1 = WeeklyPoints(week_number=1, goal_regulation=1, assists=1)
    #p1 = Player(name='Alex', init_value = 5.5, points = 0, weekly_points=[w1])
    #print p1
    #p1.save()
    #karasik = Player.objects(name='Alex K.')[0]
    #print karasik
    #team = Team(name='Kostya FC', goalkeaper=karasik, forwards=[karasik])
    #print team.name, team.goalkeaper
    #user = User(name='Kostya Dyachkov', team = team)
    #user.save()

    #players = Player.objects(name='Alex K.')
    players = Player.objects.all()
    #for p in Player.objects.all():
    #    print p.name, p.weekly_points[0].goal_regulation
    players = [(p.name, p.position, p.init_value) for p in players]
    #for p in players:
    #    print p.name, p.init_value
    context = RequestContext(request, {
        'players': players
        })
    return render_to_response('index.html', context_instance=context)


def get_players(request):
    players_obj = Player.objects.all()

    # players = [{'id':str(p.id), 'name' : p.name, 'position':p.position, 'init_value': str(p.init_value)} for p in players]

    players = []
    for player in players_obj:
        d = {
            'id': str(player.id),
            'name': player.name,
            'init_value': str(player.init_value),
            'position': player.position,
            'primary_position': player.position[0]
        }
        players.append(d)

    # players = [{'id':str(p.id), 'name' : p.name, 'primary_position':p.position[0], 'secondary_position': p.position[1] if len(p.position)>1 else '', 'third_position':len(p.position)>2 if p.position[3] else '', 'init_value': str(p.init_value)} for p in players]

    response = json.dumps({'players': players})
    return HttpResponse(response, mimetype='application/json')


def get_team(request):
    team_name = request.POST.get('team_name')
    if not team_name:
        return HttpResponse(status=500)  # TODO: return correct error

    team_obj = Team.objects.get(name=team_name)
    goalkeeper = team_obj.goalkeeper
    defenders = team_obj.defenders
    midfielders = team_obj.midfielders
    forwards = team_obj.forwards
    subs = team_obj.subs

    team_dict = {
        'goalkeer': goalkeeper,
        'defenders': defenders,
        'midfielders': midfielders,
        'forwards': forwards,
        'subs': subs
    }

    response = json.dumps({'team': team_dict})
    return HttpResponse(response, mimetype='application/json')


@csrf_exempt
def save_team(request):
    team_str = request.POST.get('team')
    team_json = json.loads(team_str)
    goalkeeper = team_json['GK']
    defenders = team_json['D']
    midfielders = team_json['M']
    forwards = team_json['F']
    subs = team_json['S']


    team_name = 'TestFC'
    team = Team(name=team_name)

    if goalkeeper:
        goalkeeper = Player.objects(id=goalkeeper[0]['id'])[0]
        team.goalkeeper = goalkeeper
    if defenders:
        defenders_objs = [Player.objects(id=defender['id']) for defender in defenders]
        team.defenders = defenders_objs
    if midfielders:
        midfielders_objs = [Player.objects(id=midfielder['id']) for midfielder in midfielders]
        team.midfielders = midfielders_objs
    if forwards:
        forwards_objs = [Player.objects(id=forward['id']) for forward in forwards]
        team.forwards = forwards_objs
    if subs:
        subs_objs = [Player.objects(id=sub['id']) for sub in subs]
        team.subs = subs_objs

    user = User(name='Kostya Dyachkov', team=team)
    user.save()


    print goalkeeper
    print defenders
    print midfielders
    print forwards
    print subs

    return HttpResponse(status=200)