# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ContentItem.protected'
        db.alter_column('fiber_contentitem', 'protected', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Adding field 'Page.alias_page'
        db.add_column('fiber_page', 'alias_page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='aliasing_pages', null=True, to=orm['fiber.Page']), keep_default=False)

        # Changing field 'Page.show_in_menu'
        db.alter_column('fiber_page', 'show_in_menu', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'Page.protected'
        db.alter_column('fiber_page', 'protected', self.gf('django.db.models.fields.BooleanField')(blank=True))


    def backwards(self, orm):
        
        # Changing field 'ContentItem.protected'
        db.alter_column('fiber_contentitem', 'protected', self.gf('django.db.models.fields.BooleanField')())

        # Deleting field 'Page.alias_page'
        db.delete_column('fiber_page', 'alias_page_id')

        # Changing field 'Page.show_in_menu'
        db.alter_column('fiber_page', 'show_in_menu', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Page.protected'
        db.alter_column('fiber_page', 'protected', self.gf('django.db.models.fields.BooleanField')())


    models = {
        'fiber.contentitem': {
            'Meta': {'object_name': 'ContentItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'fiber.file': {
            'Meta': {'object_name': 'File'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'fiber.image': {
            'Meta': {'object_name': 'Image'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'fiber.page': {
            'Meta': {'object_name': 'Page'},
            'alias_page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'aliasing_pages'", 'null': 'True', 'to': "orm['fiber.Page']"}),
            'content_items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fiber.ContentItem']", 'through': "orm['fiber.PageContentItem']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'mark_current_regexes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'named_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subpages'", 'null': 'True', 'to': "orm['fiber.Page']"}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'relative_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'fiber.pagecontentitem': {
            'Meta': {'object_name': 'PageContentItem'},
            'block_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fiber.ContentItem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'page_content_items'", 'to': "orm['fiber.Page']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fiber']
