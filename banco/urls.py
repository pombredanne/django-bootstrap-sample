'''
from django.conf.urls.defaults import *

from banco import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
'''

from django.conf.urls.defaults import *

from banco import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<banco_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<banco_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)