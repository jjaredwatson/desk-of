from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.show, name = 'show')
]
