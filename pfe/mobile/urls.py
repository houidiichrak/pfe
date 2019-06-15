from django.conf.urls import url
from  . import views

app_name='mobile'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location$', views.location, name='location'),
    url(r'^reservation$', views.reservation, name='reservation')

]
