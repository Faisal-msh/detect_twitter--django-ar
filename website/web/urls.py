from django.conf.urls import url 
from . import views

urlpatterns=[
    url('', views.home, name='Home-Page'),
    url('',views.page,name='report'),
]
