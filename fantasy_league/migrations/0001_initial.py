# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Position'
        db.create_table(u'fantasy_league_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'fantasy_league', ['Position'])

        # Adding model 'Player'
        db.create_table(u'fantasy_league_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('primary_position', self.gf('django.db.models.fields.related.ForeignKey')(related_name='primary_position', to=orm['fantasy_league.Position'])),
            ('init_value', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('current_value', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'fantasy_league', ['Player'])

        # Adding M2M table for field positions on 'Player'
        db.create_table(u'fantasy_league_player_positions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm[u'fantasy_league.player'], null=False)),
            ('position', models.ForeignKey(orm[u'fantasy_league.position'], null=False))
        ))
        db.create_unique(u'fantasy_league_player_positions', ['player_id', 'position_id'])

        # Adding model 'Team'
        db.create_table(u'fantasy_league_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('captain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='captain', to=orm['fantasy_league.Player'])),
            ('team_points', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'fantasy_league', ['Team'])

        # Adding model 'Membership'
        db.create_table(u'fantasy_league_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fantasy_league.Player'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fantasy_league.Position'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fantasy_league.Team'])),
            ('amount_paid', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('date_picked', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'fantasy_league', ['Membership'])

        # Adding model 'User'
        db.create_table(u'fantasy_league_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fantasy_league.Team'])),
        ))
        db.send_create_signal(u'fantasy_league', ['User'])


    def backwards(self, orm):
        # Deleting model 'Position'
        db.delete_table(u'fantasy_league_position')

        # Deleting model 'Player'
        db.delete_table(u'fantasy_league_player')

        # Removing M2M table for field positions on 'Player'
        db.delete_table('fantasy_league_player_positions')

        # Deleting model 'Team'
        db.delete_table(u'fantasy_league_team')

        # Deleting model 'Membership'
        db.delete_table(u'fantasy_league_membership')

        # Deleting model 'User'
        db.delete_table(u'fantasy_league_user')


    models = {
        u'fantasy_league.membership': {
            'Meta': {'object_name': 'Membership'},
            'amount_paid': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'date_picked': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Player']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Position']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Team']"})
        },
        u'fantasy_league.player': {
            'Meta': {'object_name': 'Player'},
            'current_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
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
            'captain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'captain'", 'to': u"orm['fantasy_league.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'players'", 'symmetrical': 'False', 'through': u"orm['fantasy_league.Membership']", 'to': u"orm['fantasy_league.Player']"}),
            'team_points': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'fantasy_league.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fantasy_league.Team']"})
        }
    }

    complete_apps = ['fantasy_league']