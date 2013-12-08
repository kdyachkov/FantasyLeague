# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        PLAYERS = [
            ('Alex K.', ['GK'], 6),
            ('Aaron (Yamin)', ['GK'], 5.5),
            ('Ilya K.', ['GK'], 6),
            ('Vova', ['GK'], 5.5),
            ('Manny', ['D'], 7),
            ('Zaur', ['D', 'M'], 7.5),
            ('Edik', ['D'], 6.5),
            ('Boris', ['D', 'M'], 6.5),
            ('Misha', ['D', 'M'], 6.5),
            ('Vlad', ['D'], 7),
            ('Manu', ['D', 'M'], 5.5),
            ('Andriy H.', ['D'], 6.5),
            ('Sly', ['D'], 5.5),
            ('Guri', ['D', 'M'], 6),
            ('Vitaliy', ['D'], 5.5),
            ('Dima', ['D', 'M'], 6),
            ('Little Alex', ['D'], 5),
            ('Sergiy', ['D'], 5),
            ('Andrey B.', ['D'], 7),
            ('Sonat', ['M', 'F', 'D'], 8),
            ('Rustam', ['M', 'F'], 9),
            ('Kostya', ['M'], 5.5),
            ('Alex S.', ['M', 'F'], 6.5),
            ('Elman', ['M', 'D'], 6),
            ('Yaron', ['M', 'F'], 8),
            ('Ramsay', ['M'], 8),
            ('Siroj', ['M', 'F'], 8.5),
            ('Andres', ['M', 'F'], 8.5),
            ('Edison', ['M', 'F'], 7.5),
            ('George', ['M', 'F'], 5),
            ('Juan', ['M', 'F'], 6.5),
            ('Andrew', ['M', 'D'], 9),
            ('Charlie', ['M', 'D'], 7),
            ('Oleg T.', ['F'], 9.5),
            ('Oleg K.', ['F'], 8),
            ('Atham', ['F', 'M'], 9),
            ('Sasho', ['F'], 9),
            ('Artur', ['F'], 8),
            ('Fritz', ['F'], 8.5),
            ('Malcavich', ['F'], 8.5),
            ('Efe', ['F'], 9),
        ]
        for name, positions, init_value in PLAYERS:
            print name
            player = orm.Player()
            player.name = name
            player.primary_position = orm.Position.objects.get(position=positions[0])
            player.init_value = init_value
            player.current_value = init_value
            player.save()
            player.positions = [orm.Position.objects.get(position=pos) for pos in positions]
            player.save()


    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
