from django.conf.urls import url 
from . import views

urlpatterns=[
    url('', views.home, name='Home-Page'),
    ]

    {% load static %}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel= "stylesheet" href= "{% static 'css/main.css' % }">
    </head>
    <body>
        <div>haaay guys </div> 
    </body>
</html>