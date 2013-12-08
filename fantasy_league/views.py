import json
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import datetime
from models import Player, Team, Membership
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
    if Team.objects.filter(name=team_name).exists():
        return general.generate_http_response(500, ('message', 'Team name %s already used' %team_name))


    team = Team()
    team.name = team_name
    team.money_to_spend = settings.MAX_TEAM_STARTING_VALUE
    team.save()

    user.team = team
    user.save()

    response = json.dumps({'status': 200,
                           'message': 'Team %s successfully created' %team_name})
    return HttpResponse(response, mimetype="application/json", status=200)


@csrf_exempt
def get_team(request):
    user = request.user
    if not user.is_active:
        return HttpResponse(status=401)

    team = user.team
    if not team:
        return general.generate_http_response(500, ('message', 'No team exists, please create one first'), ('team_exists', False))

    if not team.players.all():
        return general.generate_http_response(200,
                        ('message', 'team is empty'),
                        ('team_exists', True),
                        ('team_name', team.name),
                        ('players', []),
                        ('money_to_spend', float(team.money_to_spend))
        )

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

    user = request.user
    if not user.is_active:
        return HttpResponse(status=401)

    team_str = request.POST.get('team')
    team_dict = json.loads(team_str)

    team = user.team
    team.players.clear()

    for position in team_dict:
        players_ids = [p['id'] for p in team_dict[position]]
        players_objs = Player.objects.filter(id__in=players_ids)
        for player in players_objs:
            m1 = Membership(player=player, position=player.primary_position, team=team, amount_paid=player.current_value, date_picked=timezone.now())
            m1.save()


    return HttpResponse(status=200)