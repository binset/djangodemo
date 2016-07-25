from django.conf.urls import url

from . import views

app_name = "gmaps"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/(?P<location>[a-zA-Z0-9]+)/$', views.add_location, name='add_location'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_location, name='delete_location'),
    url(r'^location/new/$', views.location_new, name='location_new'),
]
