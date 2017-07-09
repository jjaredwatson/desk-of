from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.show, name = 'show'),
    url(r'^post_url/$', views.post_treasure, name="post_treasure")
]
