

def convert_player_objs(player_objs):
    if not player_objs:
        return []

    all_players = []
    for player_obj in player_objs:
        player = {
            'name': player_obj.name,
            'positions': [pos.position for pos in player_obj.positions.all()],
            'primary_position': player_obj.primary_position.position,
            'init_value': float(player_obj.init_value),
            'current_value': float(player_obj.current_value),
        }
        all_players.append(player)

    return all_players