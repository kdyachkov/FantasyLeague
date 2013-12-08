from django.db import models
from django.contrib import admin


#class WeeklyPoints(models.Model):
#    #player = ReferenceField(Player)
#    week_number = IntField()
#    points_total = DecimalField()
#    clean_sheet = IntField()
#    saves = IntField()
#    penalty_save_regulation = IntField()
#    penalty_save_tiebreaker = IntField()
#    goals_conceded = IntField()
#    goal_regulation = IntField()
#    goal_tiebreaker = IntField()
#    assist = IntField()
#    penalty_miss = IntField()
#    yellow_card = IntField()
#    red_card = IntField()
#    own_goal = IntField()


class Position(models.Model):
    position = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.position


class Player(models.Model):
    name = models.CharField(max_length=50)
    positions = models.ManyToManyField(Position, related_name='positions')
    primary_position = models.ForeignKey(Position, related_name='primary_position')
    init_value = models.DecimalField(max_digits=3, decimal_places=2)
    current_value = models.DecimalField(max_digits=3, decimal_places=2)
    #weekly_points = models.ForeignKey(Week) # TODO: need to implement this

    def __unicode__(self):
        return self.name + " (" + self.primary_position.position + ")"


class Team(models.Model):
    name = models.CharField(max_length=100,unique=True)
    players = models.ManyToManyField(Player, through="Membership", related_name='players')
    captain = models.ForeignKey(Player, related_name='captain')
    team_points = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return self.name


class Membership(models.Model):
    player = models.ForeignKey(Player)
    position = models.ForeignKey(Position)
    team = models.ForeignKey(Team)
    amount_paid = models.DecimalField(max_digits=3, decimal_places=2)
    date_picked = models.DateField()


class User(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team)

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

admin.site.register(Position)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Membership)
admin.site.register(User)

