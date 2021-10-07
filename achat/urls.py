from django.conf.urls import url
from . views import *
urlpatterns=[
       
          url(r'^indox$',indox,name='indox'),
          url(r'^display11$',display11,name='display11'),
          url(r'^display22$',display22,name='display22'),
          url(r'^display33$',display33,name='display33'),
          
          
          url(r'^delete_desktop1/(?P<pk>\d+)$',delete_desktop1,name='delete_desktop1'),
          url(r'^delete_laptop1/(?P<pk>\d+)$',delete_laptop1,name='delete_laptop1'),
          url(r'^delete_mobile1/(?P<pk>\d+)$',delete_mobile1,name='delete_mobile1'),
]