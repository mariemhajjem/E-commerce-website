from django.conf.urls import url
from . import views

app_name='Chaussure'
urlpatterns =[
    url(r'^$', views.all_shoes, name='all-shoes'),
    url(r'^(?P<id>\d+)$', views.shoe, name='shoe'),
    url(r'^shoeOnDemand$', views.shoe_on_demand, name='shoe_on_demand'),
    url(r'^(?P<id>\d+)/edit$', views.edit_shoe, name='edit_shoe'),
]
