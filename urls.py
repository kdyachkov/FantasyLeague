from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'FantasyLeague.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     # url(r'^admin/', include(admin.site.urls)),
# )
urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       (r'^', include('fantasy_league.urls')),
                       url(r'', include('social_auth.urls')),
                       #url('', include('social.apps.django_app.urls', namespace='social'))
                       )