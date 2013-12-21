# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Week'
        db.delete_table(u'fantasy_league_week')

        # Deleting field 'Game.week'
        db.delete_column(u'fantasy_league_game', 'week_id')

        # Adding field 'Game.week_number'
        db.add_column(u'fantasy_league_game', 'week_number',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Week'
        db.create_table(u'fantasy_league_week', (
            ('beginning_date', self.gf('django.db.models.fields.DateField')()),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('closing_datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'fantasy_league', ['Week'])


        # User chose to not deal with backwards NULL issues for 'Game.week'
        raise RuntimeError("Cannot reverse this migration. 'Game.week' and its values cannot be restored.")
        # Deleting field 'Game.week_number'
        db.delete_column(u'fantasy_league_game', 'week_number')


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
        u'fantasy_league.game': {
            'Meta': {'object_name': 'Game'},
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
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Position']"}),
            'red_card': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'saves': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_number': ('django.db.models.fields.IntegerField', [], {}),
            'yellow_card': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
            'games': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'weeks'", 'symmetrical': 'False', 'to': u"orm['fantasy_league.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
        }
    }

    complete_apps = ['fantasy_league']