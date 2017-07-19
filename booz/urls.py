from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.booz_list, name='booz_list'),
    url(r'^user/(?P<username>[-\w]+)/$', views.booz_user,
        name='booz_user'),
    url(r'^booz/(?P<pk>\d+)/$', views.booz_detail, name='booz_detail'),
    url(r'^create/$', views.booz_create,
        name='booz_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.booz_edit,
        name='booz_edit'),
    url(r'^booz/(?P<pk>\d+)/comment/$', views.add_comment_to_booz, name='add_comment_to_booz'),
    url(r'^booz/(?P<pk>\d+)/like/$', views.add_like_to_booz, name='add_like_to_booz'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
