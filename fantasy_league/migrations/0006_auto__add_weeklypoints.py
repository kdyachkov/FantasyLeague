# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeeklyPoints'
        db.create_table(u'fantasy_league_weeklypoints', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fantasy_league.Player'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fantasy_league.Position'])),
            ('week_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('points_total', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('clean_sheet', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('saves', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('penalty_save_regulation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('penalty_save_tiebreaker', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goals_conceded', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goal_regulation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('goal_tiebreaker', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('assist', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('penalty_miss', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('yellow_card', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('red_card', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('own_goal', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'fantasy_league', ['WeeklyPoints'])

        # Adding M2M table for field points on 'Player'
        db.create_table(u'fantasy_league_player_points', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm[u'fantasy_league.player'], null=False)),
            ('weeklypoints', models.ForeignKey(orm[u'fantasy_league.weeklypoints'], null=False))
        ))
        db.create_unique(u'fantasy_league_player_points', ['player_id', 'weeklypoints_id'])


    def backwards(self, orm):
        # Deleting model 'WeeklyPoints'
        db.delete_table(u'fantasy_league_weeklypoints')

        # Removing M2M table for field points on 'Player'
        db.delete_table('fantasy_league_player_points')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fantasy_league.membership': {
            'Meta': {'object_name': 'Membership'},
            'amount_paid': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'date_picked': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Player']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Position']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Team']"})
        },
        u'fantasy_league.player': {
            'Meta': {'object_name': 'Player'},
            'current_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'points': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'points'", 'symmetrical': 'False', 'to': u"orm['fantasy_league.WeeklyPoints']"}),
            'positions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'positions'", 'symmetrical': 'False', 'to': u"orm['fantasy_league.Position']"}),
            'primary_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_position'", 'to': u"orm['fantasy_league.Position']"})
        },
        u'fantasy_league.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'fantasy_league.team': {
            'Meta': {'object_name': 'Team'},
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'captain'", 'null': 'True', 'to': u"orm['fantasy_league.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money_to_spend': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'players'", 'symmetrical': 'False', 'through': u"orm['fantasy_league.Membership']", 'to': u"orm['fantasy_league.Player']"}),
            'team_points': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'})
        },
        u'fantasy_league.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['fantasy_league.Team']", 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'})
        },
        u'fantasy_league.weeklypoints': {
            'Meta': {'object_name': 'WeeklyPoints'},
            'assist': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'clean_sheet': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goal_regulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goal_tiebreaker': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goals_conceded': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'own_goal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'penalty_miss': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'penalty_save_regulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'penalty_save_tiebreaker': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Player']"}),
            'points_total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Position']"}),
            'red_card': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'saves': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'yellow_card': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['fantasy_league']