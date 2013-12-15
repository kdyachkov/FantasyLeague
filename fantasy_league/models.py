from decimal import Decimal
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, Group
from django.utils.http import urlquote
from django.utils import timezone

class WeeklyPoints(models.Model):
    player = models.ForeignKey('Player')
    position = models.ForeignKey('Position')
    week_number = models.IntegerField(default=0)
    points_total = models.IntegerField(default=0)
    clean_sheet = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    penalty_save_regulation = models.IntegerField(default=0)
    penalty_save_tiebreaker = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    goal_regulation = models.IntegerField(default=0)
    goal_tiebreaker = models.IntegerField(default=0)
    assist = models.IntegerField(default=0)
    penalty_miss = models.IntegerField(default=0)
    yellow_card = models.IntegerField(default=0)
    red_card = models.IntegerField(default=0)
    own_goal = models.IntegerField(default=0)


class Position(models.Model):
    position = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.position


class Player(models.Model):
    name = models.CharField(max_length=50)
    positions = models.ManyToManyField(Position, related_name='positions')
    primary_position = models.ForeignKey(Position, related_name='primary_position')
    init_value = models.DecimalField(max_digits=4, decimal_places=2)
    current_value = models.DecimalField(max_digits=4, decimal_places=2)
    weekly_points = models.ManyToManyField(WeeklyPoints, related_name='points')

    def __unicode__(self):
        return self.name + " (" + self.primary_position.position + ")"


class Team(models.Model):
    name = models.CharField(max_length=100,unique=True)
    players = models.ManyToManyField(Player, through="Membership", related_name='players')
    captain = models.ForeignKey(Player, related_name='captain', null=True)
    team_points = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    money_to_spend = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __unicode__(self):
        return self.name


class Membership(models.Model):
    player = models.ForeignKey(Player)
    position = models.ForeignKey(Position)
    team = models.ForeignKey(Team)
    amount_paid = models.DecimalField(max_digits=4, decimal_places=2)
    date_picked = models.DateField()


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    team = models.ForeignKey(Team, null=True, blank=True, default=None)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

admin.site.register(Position)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Membership)
admin.site.register(User)

