from django.conf.urls import patterns, include, url

# Admin:
from django.contrib import admin
admin.autodiscover()

# URLS:
urlpatterns = patterns('',
    url(r'^$', 'main.views.index'), # Main View
    url(r'^login$', 'users.views.login'), # Login View
    url(r'^logout$', 'users.views.logout'), # Logout View
    url(r'^ideas$', 'main.views.ideas'), # Idea View
    url(r'^signup$', 'users.view.signup'), #Signup View
    url(r'^admin/', include(admin.site.urls)), # Admin
)
