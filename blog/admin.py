from django.contrib import admin
from stepsofatraveler.blog.models import Blog, Category, PhotoAlbum

# class BlogAdmin(admin.ModelAdmin):
#     pass

# class CategoryAdmin(admin.ModelAdmin):
#     pass

# class PhotoAlbumAdmin(admin.ModelAdmin):
#     pass

# we define our resources to add to admin pages
class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/js/plugins/dojo-editor.js',
  )
  css = {
    'all': ('/static/css/dojo-editor.css',),
  }

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(PhotoAlbum)