# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FacebookComments'
        db.create_table('cmsplugin_facebookcomments', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pageurl', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('num_posts', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
        ))
        db.send_create_signal('cms_social_networks', ['FacebookComments'])

        # Adding model 'FacebookFacepile'
        db.create_table('cmsplugin_facebookfacepile', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pageurl', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
            ('max_rows', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('action', self.gf('django.db.models.fields.CharField')(default=None, max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('cms_social_networks', ['FacebookFacepile'])

        # Adding model 'FacebookLikebox'
        db.create_table('cmsplugin_facebooklikebox', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pageurl', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
            ('border_color', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('stream', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('header', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('cms_social_networks', ['FacebookLikebox'])

        # Adding model 'FacebookLike'
        db.create_table('cmsplugin_facebooklike', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pageurl', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('color_scheme', self.gf('django.db.models.fields.CharField')(default='light', max_length=50)),
            ('action', self.gf('django.db.models.fields.CharField')(default='like', max_length=50)),
            ('layout', self.gf('django.db.models.fields.CharField')(default='standard', max_length=50)),
            ('font', self.gf('django.db.models.fields.CharField')(default='arial', max_length=50)),
            ('border_color', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('send', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('cms_social_networks', ['FacebookLike'])

        # Adding model 'FacebookLoginButton'
        db.create_table('cmsplugin_facebookloginbutton', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('appId', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('show_faces', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('max_rows', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal('cms_social_networks', ['FacebookLoginButton'])

        # Adding model 'FacebookLivestream'
        db.create_table('cmsplugin_facebooklivestream', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('appId', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('event_app_id', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None, null=True, blank=True)),
            ('always_post_to_friends', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('xid', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('via_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('cms_social_networks', ['FacebookLivestream'])


    def backwards(self, orm):
        # Deleting model 'FacebookComments'
        db.delete_table('cmsplugin_facebookcomments')

        # Deleting model 'FacebookFacepile'
        db.delete_table('cmsplugin_facebookfacepile')

        # Deleting model 'FacebookLikebox'
        db.delete_table('cmsplugin_facebooklikebox')

        # Deleting model 'FacebookLike'
        db.delete_table('cmsplugin_facebooklike')

        # Deleting model 'FacebookLoginButton'
        db.delete_table('cmsplugin_facebookloginbutton')

        # Deleting model 'FacebookLivestream'
        db.delete_table('cmsplugin_facebooklivestream')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cms_social_networks.facebookcomments': {
            'Meta': {'object_name': 'FacebookComments', 'db_table': "'cmsplugin_facebookcomments'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'num_posts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cms_social_networks.facebookfacepile': {
            'Meta': {'object_name': 'FacebookFacepile', 'db_table': "'cmsplugin_facebookfacepile'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'max_rows': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cms_social_networks.facebooklike': {
            'Meta': {'object_name': 'FacebookLike', 'db_table': "'cmsplugin_facebooklike'", '_ormbases': ['cms.CMSPlugin']},
            'action': ('django.db.models.fields.CharField', [], {'default': "'like'", 'max_length': '50'}),
            'border_color': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'arial'", 'max_length': '50'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '50'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'send': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cms_social_networks.facebooklikebox': {
            'Meta': {'object_name': 'FacebookLikebox', 'db_table': "'cmsplugin_facebooklikebox'", '_ormbases': ['cms.CMSPlugin']},
            'border_color': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_scheme': ('django.db.models.fields.CharField', [], {'default': "'light'", 'max_length': '50'}),
            'header': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pageurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stream': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'cms_social_networks.facebooklivestream': {
            'Meta': {'object_name': 'FacebookLivestream', 'db_table': "'cmsplugin_facebooklivestream'", '_ormbases': ['cms.CMSPlugin']},
            'always_post_to_friends': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'appId': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'event_app_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'via_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'xid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'cms_social_networks.facebookloginbutton': {
            'Meta': {'object_name': 'FacebookLoginButton', 'db_table': "'cmsplugin_facebookloginbutton'", '_ormbases': ['cms.CMSPlugin']},
            'appId': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'max_rows': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'show_faces': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cms_social_networks']