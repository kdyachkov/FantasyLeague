from django.conf.urls import *
from views import *

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),)