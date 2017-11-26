from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductView.as_view(), name='product_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
]
