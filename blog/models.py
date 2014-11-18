from django.db import models
import os

#path to store blog post images
def get_image_path(instance, filename):
    return os.path.join('blogposts', filename)

#path to store photo album cover images
def get_album_image_path(instance, filename):
    return os.path.join('photoalbum', filename)

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30, unique=True)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Category')
    views = models.IntegerField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to=get_image_path)
    img_title = models.CharField(max_length=100, null=True)
    img_alt = models.CharField(max_length=200, null=True)
    active = models.BooleanField()
    show_pic = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-post_date']

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    views = models.IntegerField(editable=False, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

class PhotoAlbum(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to=get_album_image_path)
    img_title = models.CharField(max_length=100, null=True)
    img_alt = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['title']