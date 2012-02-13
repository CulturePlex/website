# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('web_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('googleplus', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('web', ['Person'])

        # Adding model 'Project'
        db.create_table('web_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Person'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('incarousel', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('web', ['Project'])

        # Adding M2M table for field members on 'Project'
        db.create_table('web_project_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['web.project'], null=False)),
            ('person', models.ForeignKey(orm['web.person'], null=False))
        ))
        db.create_unique('web_project_members', ['project_id', 'person_id'])

        # Adding model 'Publication'
        db.create_table('web_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aceptation_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('keywords', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hosted_at', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('url_hosted_at', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('publication_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('web', ['Publication'])

        # Adding M2M table for field authors on 'Publication'
        db.create_table('web_publication_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publication', models.ForeignKey(orm['web.publication'], null=False)),
            ('person', models.ForeignKey(orm['web.person'], null=False))
        ))
        db.create_unique('web_publication_authors', ['publication_id', 'person_id'])

        # Adding M2M table for field related_projects on 'Publication'
        db.create_table('web_publication_related_projects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('publication', models.ForeignKey(orm['web.publication'], null=False)),
            ('project', models.ForeignKey(orm['web.project'], null=False))
        ))
        db.create_unique('web_publication_related_projects', ['publication_id', 'project_id'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('web_person')

        # Deleting model 'Project'
        db.delete_table('web_project')

        # Removing M2M table for field members on 'Project'
        db.delete_table('web_project_members')

        # Deleting model 'Publication'
        db.delete_table('web_publication')

        # Removing M2M table for field authors on 'Publication'
        db.delete_table('web_publication_authors')

        # Removing M2M table for field related_projects on 'Publication'
        db.delete_table('web_publication_related_projects')


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
            'aceptation_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'-'", 'symmetrical': 'False', 'to': "orm['web.Person']"}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'hosted_at': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'publication_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'related_projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'-'", 'blank': 'True', 'to': "orm['web.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url_hosted_at': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['web']
