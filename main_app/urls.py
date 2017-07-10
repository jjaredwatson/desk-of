from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.desk),
    url(r'^drinks/$', views.index_drink),
    url(r'^([0-9]+)/$', views.show_drink, name = 'show'),
    url(r'^drinks/post_url/$', views.post_drink, name="post_drink"),
    url(r'^journal/$', views.index_journal),
    url(r'^([0-9]+)/$', views.show_journal, name = 'show'),
    url(r'^journal/post_url/$', views.post_journal, name="post_journal")
]
