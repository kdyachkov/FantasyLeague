from django.conf.urls import *
from views import *

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
	                   url(r'^get_players/$', get_players, name='get_players'),
                       url(r'^save_team/$', save_team, name='save_team'),
                       url(r'^get_team/$', get_team, name='get_team'),
                       url(r'^create_team/$', create_team, name='create_team'),
                       url(r'^login-error/$', login_error, name='login-error'),
                       url(r'^logoff/$', logoff, name='logoff'),

                       )