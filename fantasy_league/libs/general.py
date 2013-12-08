import json
from django.http import HttpResponse

def convert_player_objs(player_objs):
    if not player_objs:
        return []

    all_players = []
    for player_obj in player_objs:
        player = {
            'id': player_obj.id,
            'name': player_obj.name,
            'positions': [pos.position for pos in player_obj.positions.all()],
            'primary_position': player_obj.primary_position.position,
            'init_value': float(player_obj.init_value),
            'current_value': float(player_obj.current_value),
        }
        all_players.append(player)

    return all_players


def generate_http_response(status, *args):
    data = {name: val for name, val in args}
    data['status'] = status
    response = json.dumps(data)
    return HttpResponse(response, mimetype="application/json", status=status)