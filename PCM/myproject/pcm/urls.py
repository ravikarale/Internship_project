from django.conf.urls import url

from .import views


urlpatterns = [

	url(r'^$', views.pcm_home , name='pcm_home'),
	#url(r'^add/$', 'pcm.views.add' , name='add'),
	#url(r'^hello/$', 'pcm.views.hello',name='hello'),
	#url(r'^home/$', 'pcm.views.home',name='home'),
	url(r'^home', views.home, name='home'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^model_form_upload/$', views.model_form_upload, name='model_form_upload'),
]