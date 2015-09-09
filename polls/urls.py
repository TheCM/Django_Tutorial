from django.conf.urls import url

from . import views

ulrpatterns = [
  url(r'^$', views.index, name='index')
]
