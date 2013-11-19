from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Player, WeeklyPoints, Team, User

def index(request):

    #w1 = WeeklyPoints(week_number=1, goal_regulation=1, assists=1)
    #p1 = Player(name='Alex', init_value = 5.5, points = 0, weekly_points=[w1])
    #print p1
    #p1.save()
    karasik = Player.objects(name='Alex K.')[0]
    print karasik
    team = Team(name='Kostya FC', goalkeaper=karasik, forwards=[karasik])
    print team.name, team.goalkeaper
    user = User(name='Kostya Dyachkov', team = team)
    user.save()

    players = Player.objects(name='Alex K.')
    #players = Player.objects.all()
    #for p in Player.objects.all():
    #    print p.name, p.weekly_points[0].goal_regulation
    for p in players:
        print p.name, p.init_value
    context = RequestContext(request, {
        'players': players
        })
    return render_to_response('index.html', context_instance=context)