from django.db import models
from mongoengine import *



class WeeklyPoints(EmbeddedDocument):
    #player = ReferenceField(Player)
    week_number = IntField()
    points_total = DecimalField()
    clean_sheet = IntField()
    saves = IntField()
    penalty_save_regulation = IntField()
    penalty_save_tiebreaker = IntField()
    goals_conceded = IntField()
    goal_regulation = IntField()
    goal_tiebreaker = IntField()
    assist = IntField()
    penalty_miss = IntField()
    yellow_card = IntField()
    red_card = IntField()
    own_goal = IntField()


class Player(Document):
    name = StringField(required=True)
    position = ListField(StringField(max_length=30))
    init_value = DecimalField()
    current_value = DecimalField()
    weekly_points = ListField(EmbeddedDocumentField(WeeklyPoints))


class Team(EmbeddedDocument):
    name = StringField(required=True)
    goalkeeper = ListField(ReferenceField(Player))
    defenders = ListField(ReferenceField(Player))
    midfielders = ListField(ReferenceField(Player))
    forwards = ListField(ReferenceField(Player, dbref=True))
    subs = ListField(ReferenceField(Player))
    captain = ReferenceField(Player)
    team_points = DecimalField()


class User(Document):
    name = StringField(required=True, unique=True)
    team = EmbeddedDocumentField(Team)
    meta = {
        'indexes': ['name']  # TODO: indexes don't work, not sure why
    }
