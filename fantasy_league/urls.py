from django.conf.urls import *
from views import *

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^get_players/$', get_players, name='get_players'),)