from django.conf.urls.defaults import patterns, include, url
from stepsofatraveler.blog import views
# from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/$', views.home),
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^about/$', views.about),
    url(r'^archive/$', views.archive),
    url(r'^contact/$', views.contact),
    url(r'^overview/$', views.overview),
    url(r'^post/(\d+)', views.post, name="post"),
    url(r'^category/(\w+)$', views.category),
    url(r'^category/$', views.category),
    url(r'^photoalbums/$', views.photoalbum),
    url(r'^stats/$', views.stats),
    # This is going to be our home view.
    # We'll uncomment it later
    url(r'^$', 'stepsofatraveler.blog.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()