# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table('blog_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('post_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, db_index=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('views', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('blog', ['Blog'])

        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('blog_blog')

        # Deleting model 'Category'
        db.delete_table('blog_category')


    models = {
        'blog.blog': {
            'Meta': {'ordering': "['post_date']", 'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']