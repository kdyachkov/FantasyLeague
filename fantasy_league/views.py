import json
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from models import Player, Team, User
from libs import general


def index(request):
    context = RequestContext(request, {})
    return render_to_response('index.html', context_instance=context)


def logoff(request):
    logout(request)
    return render_to_response('index.html',  context_instance=RequestContext(request))

def login_error(request):
    #error = get_message(request, exception)
    return render_to_response('index.html', context_instance=RequestContext(request))


def get_players(request):
    all_players = general.convert_player_objs(Player.objects.all())

    response = json.dumps({'players': all_players})
    return HttpResponse(response, mimetype='application/json')


@csrf_exempt
def create_team(request):
    user = request.user
    if not user.is_active:
        return HttpResponse(status=401)

    team_name = request.POST.get('team_name')
    team = Team()
    team.name = team_name

    #user_name =


@csrf_exempt
def get_team(request):
    user = request.user
    if not user.is_active:
        return HttpResponse(status=401)


    username = 'kdyachkov'
    user_objs = User.objects(name=username)
    if user_objs:
        if len(user_objs) > 1:
            return HttpResponse(status=500)
        else:
            user = user_objs[0]
            team = user.team
    else:
        return HttpResponse(status=500)

    goalkeeper = general.convert_player_objs(team.goalkeeper)
    defenders = general.convert_player_objs(team.defenders)
    midfielders = general.convert_player_objs(team.midfielders)
    forwards = general.convert_player_objs(team.forwards)
    subs = general.convert_player_objs(team.subs)

    team_dict = {
        'goalkeeper': goalkeeper,
        'defenders': defenders,
        'midfielders': midfielders,
        'forwards': forwards,
        'subs': subs,
        'max_team_starting_value': settings.MAX_TEAM_STARTING_VALUE
    }

    response = json.dumps({'team': team_dict})
    return HttpResponse(response, mimetype='application/json')


@csrf_exempt
def save_team(request):
    team_str = request.POST.get('team')
    team_json = json.loads(team_str)
    goalkeepers = team_json['GK']
    defenders = team_json['D']
    midfielders = team_json['M']
    forwards = team_json['F']
    subs = team_json['S']


    username = 'kdyachkov'
    team_name = 'TestFC'


    user = None
    team = None
    user_objs = User.objects(name=username)
    if user_objs:
        if len(user_objs) > 1:
            return HttpResponse(status=500)
        else:
            user = user_objs[0]
            team = user.team
    else:
        user = User(name=username)
        team = Team(name=team_name)
        user.team = team
        user.save()


    goalkeeper = Player.objects(id__in=[goalkeeper['id'] for goalkeeper in goalkeepers]) if goalkeepers else []
    defenders_objs = Player.objects(id__in=[defender['id'] for defender in defenders]) if defenders else []
    midfielders_objs = Player.objects(id__in=[midfielder['id'] for midfielder in midfielders]) if midfielders else []
    forwards_objs = Player.objects(id__in=[forward['id'] for forward in forwards]) if forwards else []
    subs_objs = Player.objects(id__in=[sub['id'] for sub in subs]) if subs else []

    team.goalkeeper = goalkeeper
    team.defenders = defenders_objs
    team.midfielders = midfielders_objs
    team.forwards = forwards_objs
    team.subs = subs_objs

    user.team = team
    user.save()

    print goalkeeper
    print defenders
    print midfielders
    print forwards
    print subs

    return HttpResponse(status=200)