# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.img_title'
        db.add_column('blog_blog', 'img_title',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Blog.img_alt'
        db.add_column('blog_blog', 'img_alt',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.img_title'
        db.delete_column('blog_blog', 'img_title')

        # Deleting field 'Blog.img_alt'
        db.delete_column('blog_blog', 'img_alt')


    models = {
        'blog.blog': {
            'Meta': {'ordering': "['-post_date']", 'object_name': 'Blog'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_alt': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'img_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'post_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'blog.photoalbum': {
            'Meta': {'ordering': "['title']", 'object_name': 'PhotoAlbum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img_alt': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'img_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']