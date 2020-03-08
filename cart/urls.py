from django.conf.urls import url, include
from .views import view_cart, add_to_cart, adjust_cart, delete_cart_item
from django.urls import path, include

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^delete/(?P<id>\d+)', delete_cart_item, name='delete_cart_item'),
]


# update to path before subit