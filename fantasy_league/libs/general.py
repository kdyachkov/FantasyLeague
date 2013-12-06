

def convert_player_objs(player_objs):
    if not player_objs:
        return []

    players = []
    for player in player_objs:
        d = {
            'id': str(player.id),
            'name': player.name,
            'init_value': str(player.init_value),
            'position': player.position,
            'primary_position': player.position[0]
        }
        players.append(d)

    return players