# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Publication.aceptation_date'
        db.alter_column('web_publication', 'aceptation_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Publication.publication_date'
        db.alter_column('web_publication', 'publication_date', self.gf('django.db.models.fields.DateField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Publication.aceptation_date'
        db.alter_column('web_publication', 'aceptation_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 2, 10)))

        # Changing field 'Publication.publication_date'
        db.alter_column('web_publication', 'publication_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2012, 2, 10)))


    models = {
        'web.person': {
            'Meta': {'object_name': 'Person'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'googleplus': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'web.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Person']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'incarousel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': "orm['web.Person']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'web.publication': {
            'Meta': {'object_name': 'Publication'},
            'abstract': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'aceptation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'-'", 'symmetrical': 'False', 'to': "orm['web.Person']"}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'hosted_at': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publication_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'related_projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'-'", 'blank': 'True', 'to': "orm['web.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url_hosted_at': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['web']
