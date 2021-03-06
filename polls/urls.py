
from django.conf.urls import url

from . import views

urlpatterns = [
  #example: /polls/
  url(r'^$', views.IndexView.as_view(),  name = 'index'),
  #example: /polls/5/
  url(r'^(?P<poll_id>[0-9]+)/$', views.detail,  name = 'detail'),  
  #example: /polls/5/results/
  url(r'^(?P<poll_id>[0-9]+)/results/$', views.results,  name = 'results'),
  #example: /polls/5/vote
  url(r'^(?P<poll_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
