from django.db import models
from mongoengine.django.auth import User
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

#class CustomUser(models.Model):
#    username = models.CharField(unique=True, max_length=45, db_index=True)
#    first_name = models.CharField(max_length=45)
#    last_name = models.CharField(max_length=45)
#    email = models.EmailField(unique=True)
#    status = models.SmallIntegerField()
#    activation_code = models.CharField(max_length=50, null=True, blank=True)
#    is_active = models.BooleanField(default=False)
#    is_staff = models.BooleanField(default=False)
#    created_at = models.DateTimeField(auto_now_add=True, editable=False)
#    updated_at = models.DateTimeField(auto_now=True)
#    login_at = models.DateTimeField()
#
#    def __unicode__(self):
#        return self.username
#
#    def get_fullname(self):
#        return '%s %s' % (self.first_name, self.last_name)
#
#    def get_shortname(self):
#        return self.first_name
#
#    def __meta__(self):
#        return self.username
#
#    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['email']
#
#    class Meta:
#        """Meta data"""
#        unique_together = ('username', 'first_name')