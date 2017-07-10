from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.desk),
    url(r'^drinks/$', views.index_drink),
    url(r'^drinks/([0-9]+)/$', views.show_drink, name = 'show_drink'),
    url(r'^drinks/post_url/$', views.post_drink, name="post_drink"),
    url(r'^journal/$', views.index_journal),
    url(r'^journal/([0-9]+)/$', views.show_journal, name = 'show_journal'),
    url(r'^journal/post_url/$', views.post_journal, name="post_journal")
]
