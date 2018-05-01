import sys
sys.path.append(u'/home/worksite/PyApp/makEasy/')


from django.conf.urls import url
from . import views
from . import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'item/create$', views.item, name='item'),
    url(r'item/estimate$', views.estimate, name='estimate'),
    url(r'new', ajax.new),
    url(r'getJson', ajax.getJson),
    url(r'sendOffer', ajax.sendOffer),
    url(r'createItem',ajax.createItem),
    url(r'exportDXF',ajax.exportDXF),
]