from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^create$', views.product_create, name='product_create'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/delete/$', views.product_delete, name='product_delete'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/update/$', views.product_update, name='product_update'),
]
