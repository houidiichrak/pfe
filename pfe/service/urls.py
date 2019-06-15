from django.conf.urls import url
from  . import views

app_name='service'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name='about'),
    url(r'^categorie$', views.categorie, name='categorie'),
    url(r'^region$', views.region, name='region'),
    url(r'^notfoundpage$', views.notfoundpage, name='notfoundpage'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout_user, name='logout_user'),
    url(r'^listsworker$', views.listsworker, name='listsworker'),
    url(r'^agent$', views.agent, name='agent'),
    url(r'^reserver$', views.reserver, name='reserver') 

]
