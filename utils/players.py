
# players = [
#     {'name': 'Kostya', 'position':'M', 'value': 5.5},

# ]*\

players = "Alex K., GK, 6*\
Aaron(Yamin), GK, 5.5*\
Ilya K., GK, 6*\
Vova, GK, 5.5*\
Manny, D, 7*\
Zaur, D|M, 7.5*\
Edik, D, 6.5*\
Boris, D|M, 6.5*\
Misha, D|M, 6.5*\
Vlad, D, 7*\
Manu, D|M, 5.5*\
Andriy H., D, 6.5*\
Sly, D, 5.5*\
Guri, D|M, 6*\
Vitaliy, D, 5.5*\
Dima, D|M, 6*\
Little Alex, D, 5*\
Sergiy, D, 5*\
Andrey B., D, 7*\
Sonat, M|F|D, 8*\
Rustam, M|F, 9*\
Kostya, M, 5.5*\
Alex S., M|F, 6.5*\
Elman, M|D, 6*\
Yaron, M|F, 8*\
Ramsay, M, 8*\
Siroj, M|F, 8.5*\
Andres, M|F, 8.5*\
Edison, M|F, 7.5*\
George, M|F, 5*\
Juan, M|F, 6.5*\
Andrew, M|D, 9*\
Charlie, M|D, 7*\
Oleg T., F, 9.5*\
Oleg K., F, 8*\
Atham, F|M, 9*\
Sasho, F, 9*\
Artur, F, 8*\
Fritz, F, 8.5*\
Malcavich, F, 8.5*\
Efe, F, 9"


def get_players_dict():
    player_list = []
    for player in players.split('*'):
        name, position, value = player.split(',')
        player_list.append({'name': name, 'position': [pos.strip() for pos in position.split('|')], 'init_value': value})

    # print player_list
    return player_list

get_players_dict()