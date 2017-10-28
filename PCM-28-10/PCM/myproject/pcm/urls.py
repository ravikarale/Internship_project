from django.conf.urls import url

from .import views


urlpatterns = [

	url(r'^$', views.pcm_login , name='pcm_login'),
	url(r'^pcm_home/$', views.pcm_home , name='pcm_home'),
	url(r'^index/$', views.index, name='index'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^getLogin/$', views.getLogin, name='getLogin'),
	url(r'^pcm_criteria/$', views.pcm_criteria, name='pcm_criteria'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^desplayFinal/$', views.desplayFinal, name='desplayFinal'),
	url(r'^desplayIntern/$', views.desplayIntern, name='desplayIntern'),
	# url(r'^getSelected/$', views.getSelected, name='getSelected'),
	url(r'^sendTo/$', views.sendTo, name='sendTo'),

]