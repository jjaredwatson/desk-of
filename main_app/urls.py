from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$', views.desk),
    url(r'^drinks/$', views.index_drink),
    url(r'^drinks/([0-9]+)/$', views.show_drink, name = 'show_drink'),
    url(r'^drinks/post_url/$', views.post_drink, name="post_drink"),
    url(r'^drinks/delete/(?P<pk>\d+)$', views.delete_drink, name='delete_drink'),
    url(r'^journal/$', views.index_journal),
    url(r'^journal/([0-9]+)/$', views.show_journal, name = 'show_journal'),
    url(r'^journal/post_url/$', views.post_journal, name="post_journal"),
    url(r'^journal/edit/(?P<pk>\d+)$', views.update_drink, name='edit_drink'),
    url(r'^journal/delete/(?P<pk>\d+)$', views.delete_journal, name='delete_journal'),

    url(r'^ipod/$', views.index_ipod),
    url(r'^ipod/([0-9]+)/$', views.show_ipod, name = 'show_ipod'),
    url(r'^ipod/post_url/$', views.post_ipod, name="post_ipod"),
    url(r'^ipod/delete/(?P<pk>\d+)$', views.delete_ipod, name='delete_ipod')

]
