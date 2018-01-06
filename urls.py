from django.conf.urls import url

from . import views
from . import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'item/create$', views.item, name='item'),
    url(r'new', ajax.new),
]